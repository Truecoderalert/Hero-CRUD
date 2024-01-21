from flask_app import app
from flask import Flask, request, render_template, redirect, session
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.models_hero import Hero



@app.route('/')
def askforinfo():
    return render_template('hero_form.html')


@app.route('/hero/new'  , methods = ['post'])
def redirecttoshowinfo():
    data =  {'first_name':request.form['first_name'], 'last_name':request.form['last_name'], 'alias':request.form['alias'] , 'origin':request.form['origin'] }
    Hero.create(data)
    return redirect('/hero/show')


@app.route('/hero/show')
def showinfo():
    heros = Hero.get_all()
    return render_template('display_heros.html' , heros = heros)

@app.route('/edit/<int:hero_id>')
def editinfo(hero_id):
    data = {'id':hero_id}
    hero = Hero.get_one(data)
    return render_template('edit_hero.html' , hero = hero)

@app.route('/update/<int:hero_id>', methods = ['post'])
def Update(hero_id):
    data = {'first_name':request.form['first_name'], 'last_name':request.form['last_name'],'origin':request.form['origin'], 'alias':request.form['alias'] }
    Hero.update(request.form , hero_id)
    return redirect('/hero/show')

