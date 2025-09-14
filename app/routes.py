from flask import render_template, request, redirect, url_for, flash, jsonifyfrom flask import render_template, request, redirect, url_for, flash, jsonify

from app import app, db, Postfrom app import app, db, Post

from app.utils.plant_research import PlantResearchAssistantfrom app.utils.plant_research import PlantResearchAssistant

from app.utils.plant_suggestions import PLANT_DATAfrom app.utils.plant_suggestions import PLANT_DATA

from app.utils.priority_plants import PRIORITY_PLANTS, get_priority_plantfrom app.utils.priority_plants import PRIORITY_PLANTS

from fuzzywuzzy import fuzzfrom fuzzywuzzy import fuzz

import markdown2import random

import jsonimport markdown2

import randomimport json



plant_researcher = PlantResearchAssistant()plant_researcher = PlantResearchAssistant()



@app.route('/')@app.route('/')

def index():def index():

    posts = Post.query.order_by(Post.created_at.desc()).all()    posts = Post.query.order_by(Post.created_at.desc()).all()

    return render_template('index.html', posts=posts)    return render_template('index.html', posts=posts)



@app.route('/post/<int:post_id>')@app.route('/post/<int:post_id>')

def post(post_id):def post(post_id):

    post = Post.query.get_or_404(post_id)    post = Post.query.get_or_404(post_id)

    content = markdown2.markdown(post.content)    content = markdown2.markdown(post.content)

    source_urls = json.loads(post.source_urls) if post.source_urls else []    source_urls = json.loads(post.source_urls) if post.source_urls else []

    return render_template('post.html', post=post, content=content, source_urls=source_urls)    return render_template('post.html', post=post, content=content, 

                         source_urls=source_urls)

@app.route('/create', methods=('GET', 'POST'))

def create():@app.route('/create', methods=('GET', 'POST'))

    if request.method == 'POST':def create():

        creation_mode = request.form.get('creation_mode', 'manual')    if request.method == 'POST':

        title = request.form.get('title')        creation_mode = request.form.get('creation_mode', 'manual')

        scientific_name = request.form.get('scientific_name', '')        title = request.form.get('title')

        scientific_name = request.form.get('scientific_name', '')

        if not title:

            flash('Title is required!')        if creation_mode == 'mrjblack':

            return render_template('create.html')            # MrJBlack mode: select a random priority plant if none specified

            if not title:

        if creation_mode == 'mrjblack':                plant = random.choice(PRIORITY_PLANTS)

            # Find the specified plant in priority list                title = plant['common_name']

            plant = get_priority_plant(title) or get_priority_plant(scientific_name)                scientific_name = plant['scientific_name']

                        else:

            if not plant:                # Find the specified plant in priority list

                # Try fuzzy matching if exact match not found                plant = next((p for p in PRIORITY_PLANTS 

                best_match = None                            if p['common_name'].lower() == title.lower() or 

                best_score = 0                            p['scientific_name'].lower() == scientific_name.lower()), None)

                for p in PRIORITY_PLANTS:                if not plant:

                    common_score = fuzz.ratio(title.lower(), p['common_name'].lower())                    flash('Please select a plant from the priority list!')

                    scientific_score = fuzz.ratio(scientific_name.lower(), p['scientific_name'].lower())                    return render_template('create.html')

                    score = max(common_score, scientific_score)            

                    if score > best_score and score > 80:  # 80% similarity threshold            # Generate article using AI with priority plant info

                        best_score = score            article_data = plant_researcher.generate_article(

                        best_match = p                title,

                                scientific_name,

                if best_match:                extra_context=f"This plant is {plant['conservation_status']} and {plant['trade_status']}. "

                    plant = best_match                            f"It belongs to the category of {plant['category']} and is found in {plant['habitat']}. "

                else:                            f"{plant['description']}"

                    flash('Please select a plant from the priority list!')            )

                    return render_template('create.html')            post = Post(

                            title=article_data['title'],

            # Use plant data for article generation                scientific_name=article_data['scientific_name'],

            title = plant['common_name']                content=article_data['content'],

            scientific_name = plant['scientific_name']                source_urls=json.dumps(article_data['sources']),

                            categories=plant['category'],

            # Generate article using AI with priority plant info                is_ai_generated=True,

            article_data = plant_researcher.generate_article(                author='MrJBlack'

                title,             )

                scientific_name,        elif creation_mode == 'ai':

                extra_context=f"Conservation Status: {plant['conservation_status']}\n"            if not title:

                             f"Trade Status: {plant['trade_status']}\n"                flash('Title is required!')

                             f"Region: {plant['region']}\n"                return render_template('create.html')

                             f"Export Notes: {plant['export_notes']}"            

            )            # Standard AI-generated article

                        article_data = plant_researcher.generate_article(title, scientific_name)

            post = Post(            post = Post(

                title=article_data['title'],                title=article_data['title'],

                scientific_name=article_data['scientific_name'],                scientific_name=article_data['scientific_name'],

                content=article_data['content'],                content=article_data['content'],

                source_urls=json.dumps(article_data['sources']),                source_urls=json.dumps(article_data['sources']),

                categories='South African Plants',                categories='South African Plants',

                is_ai_generated=True,                is_ai_generated=True,

                author='MrJBlack'                author='AI Assistant'

            )            )

        else:

        elif creation_mode == 'ai':            # Manual creation

            # Standard AI generation            if not title:

            article_data = plant_researcher.generate_article(title, scientific_name)                flash('Title is required!')

            post = Post(                return render_template('create.html')

                title=article_data['title'],        

                scientific_name=article_data['scientific_name'],        if use_ai:

                content=article_data['content'],            # Generate article using AI research assistant

                source_urls=json.dumps(article_data['sources']),            article_data = plant_researcher.generate_article(title, scientific_name)

                categories='South African Plants',            post = Post(

                is_ai_generated=True,                title=article_data['title'],

                author='AI Assistant'                scientific_name=article_data['scientific_name'],

            )                content=article_data['content'],

                        source_urls=json.dumps(article_data['sources']),

        else:                categories='South African Plants',

            # Manual content creation                is_ai_generated=True

            content = request.form.get('content', '')            )

            if not content:        else:

                flash('Content is required for manual creation!')            # Manual content creation

                return render_template('create.html')            content = request.form.get('content', '')

                            if not content:

            post = Post(                flash('Content is required for manual creation!')

                title=title,                return render_template('create.html')

                scientific_name=scientific_name,                

                content=content,            post = Post(

                categories=request.form.get('categories', 'South African Plants'),                title=title,

                image_url=request.form.get('image_url', ''),                scientific_name=scientific_name,

                is_ai_generated=False,                content=content,

                author=request.form.get('author', 'Anonymous')                categories=request.form.get('categories', 'South African Plants'),

            )                image_url=request.form.get('image_url', ''),

                        is_ai_generated=False,

        try:                author='Manual Author'

            db.session.add(post)            )

            db.session.commit()        

            if creation_mode == 'mrjblack':        try:

                flash('Article successfully generated by MrJBlack!')            db.session.add(post)

            elif creation_mode == 'ai':            db.session.commit()

                flash('Article successfully generated by AI Assistant!')            if creation_mode in ['ai', 'mrjblack']:

            else:                flash('Article successfully generated and published!')

                flash('Article successfully created!')            else:

            return redirect(url_for('post', post_id=post.id))                flash('Article successfully created!')

        except Exception as e:            return redirect(url_for('post', post_id=post.id))

            db.session.rollback()        except Exception as e:

            flash(f'Error creating article: {str(e)}')            db.session.rollback()

            return render_template('create.html')            flash(f'Error creating article: {str(e)}')

            return render_template('create.html')

    return render_template('create.html')

    return render_template('create.html')

@app.route('/api/plants', methods=['GET'])

def get_plants():@app.route('/api/plants', methods=['GET'])

    """Return list of plants for autocomplete with fuzzy matching"""def get_plants():

    query = request.args.get('q', '').lower()    """Return list of plants for autocomplete with fuzzy matching"""

    if not query:    query = request.args.get('q', '').lower()

        return jsonify([])    if not query:

        return jsonify([])

    # Combine priority plants and general plant data

    all_plants = []    suggestions = []

        for plant in PLANT_DATA:

    # Add priority plants first        common_ratio = fuzz.partial_ratio(query, plant['common_name'].lower())

    for plant in PRIORITY_PLANTS:        scientific_ratio = fuzz.partial_ratio(query, plant['scientific_name'].lower())

        common_ratio = fuzz.partial_ratio(query, plant['common_name'].lower())        

        scientific_ratio = fuzz.partial_ratio(query, plant['scientific_name'].lower())        if common_ratio > 60 or scientific_ratio > 60:  # Threshold for fuzzy matching

                    suggestions.append({

        if common_ratio > 60 or scientific_ratio > 60:  # Threshold for fuzzy matching                'common_name': plant['common_name'],

            all_plants.append({                'scientific_name': plant['scientific_name'],

                'common_name': plant['common_name'],                'type': plant['type'],

                'scientific_name': plant['scientific_name'],                'score': max(common_ratio, scientific_ratio)

                'type': plant['type'],            })

                'score': max(common_ratio, scientific_ratio),    

                'priority': True    # Sort by match score

            })    suggestions.sort(key=lambda x: x['score'], reverse=True)

        # Remove score from response

    # Add other plants    for s in suggestions:

    for plant in PLANT_DATA:        del s['score']

        if (query in plant['common_name'].lower() or     

            query in plant['scientific_name'].lower()):    return jsonify(suggestions[:5])  # Limit to top 5 matches

            all_plants.append({

                'common_name': plant['common_name'],@app.route('/preview', methods=['POST'])

                'scientific_name': plant['scientific_name'],def preview_article():

                'type': plant['type'],    title = request.form.get('title')

                'score': 50,  # Lower base score for non-priority plants    scientific_name = request.form.get('scientific_name')

                'priority': False    

            })    if not title:

            return jsonify({'error': 'Title is required'}), 400

    # Sort by score and priority status        

    all_plants.sort(key=lambda x: (x['priority'], x['score']), reverse=True)    try:

            article_data = plant_researcher.generate_article(title, scientific_name)

    # Remove score and priority from response        preview_content = markdown2.markdown(article_data['content'])

    for plant in all_plants:        return jsonify({

        del plant['score']            'content': preview_content,

        del plant['priority']            'sources': article_data['sources']

            })

    return jsonify(all_plants[:10])  # Limit to top 10 matches    except Exception as e:

        return jsonify({'error': str(e)}), 500

@app.route('/preview', methods=['POST'])

def preview_article():@app.route('/api/search_plant')

    title = request.form.get('title')def search_plant():

    scientific_name = request.form.get('scientific_name')    query = request.args.get('q', '')

    creation_mode = request.form.get('creation_mode', 'ai')    if not query:

            return jsonify([])

    if not title:    

        return jsonify({'error': 'Title is required'}), 400    # Search for plant data using the plant_researcher instance

        try:

    try:        article_data = plant_researcher.generate_article(query, '')

        extra_context = None        return jsonify({

        if creation_mode == 'mrjblack':            'title': article_data['title'],

            plant = get_priority_plant(title) or get_priority_plant(scientific_name)            'summary': article_data['content'][:200] + '...',

            if plant:            'url': article_data['sources'][0] if article_data['sources'] else None

                extra_context = f"Conservation Status: {plant['conservation_status']}\n"\        })

                              f"Trade Status: {plant['trade_status']}\n"\    except Exception as e:

                              f"Region: {plant['region']}\n"\        return jsonify({'error': str(e)}), 500

                              f"Export Notes: {plant['export_notes']}"    return jsonify(None)
        
        article_data = plant_researcher.generate_article(title, scientific_name, extra_context=extra_context)
        preview_content = markdown2.markdown(article_data['content'])
        return jsonify({
            'content': preview_content,
            'sources': article_data['sources']
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500