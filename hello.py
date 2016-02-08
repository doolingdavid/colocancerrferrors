from flask import Flask, render_template, session, redirect, url_for
from flask import request
from flask import make_response
from flask import redirect
from flask import abort
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from datetime import datetime
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from wtforms import BooleanField, SelectField, RadioField
from wtforms import FloatField
import pickle
import os
import numpy as np
from sklearn.externals import joblib
import pandas as pd
from pandas import Series, DataFrame
import urllib2, json
from flask import make_response
from functools import wraps, update_wrapper
from datetime import datetime
import time
import datetime
import tornado.wsgi
import tornado.httpserver
import tornado.ioloop               
import tornado.options
import tornado.autoreload
from flask import jsonify








yoblistlabel = [str(a) for a in range(1880,2020)]
yoblistchoices = zip(yoblistlabel, yoblistlabel)


yodlistlabel = [str(a) for a in range(1970,2020)]
yodlistchoices = zip(yodlistlabel, yodlistlabel)


monthlistlabel = [str(a) for a in range(1,13)]
monthlistchoices = zip(monthlistlabel, monthlistlabel)

numprimarieslistlabel = [str(a) for a in range(1,10)]
numprimarieslistchoices = zip(numprimarieslistlabel, numprimarieslistlabel)






class NameForm(Form):
            
    
    
    cs_tumor_size = FloatField('What is the tumor size (mm)?', validators=[Required()])
    address = StringField("What is the patient's address?", validators=[Required()])
    
    grade = SelectField('Grade',default='0',
                    choices = [('ce','cell type not determined'),
                        ('mo','moderately differentiated'),
                               ('po','poorly differentiated'),
                               ('un','undifferentiated; anaplastic'),
                               ('we','well differentiated'),
                               ('not','None of the above')],
                        validators=[Required()])


    hist = SelectField('Histology', default='0',
                choices = [('acinar','acinar cell neoplasms'),
                    ('adenomas','adenomas and adenocarcinomas'),
                           ('blood','blood vessel tumors'),
                           ('complex_epithelial','complex epithelial neoplasms'),
                           ('complex_mixed','complex mixed and stromal neoplasms'),
                           ('cystic','cystic, mucinous and serous neoplasms'),
                           ('ductal','ductal and lobular neoplasms'),
                           ('epithelial','epithelial neoplasms, NOS'),
                           ('fibromatuos','fibromatuos neoplasms'),
                           ('germ','germ cell neoplasms'),
                           ('lipomatous','lipomatous neoplasms'),
                           ('misc_bone','miscellaneous bone tumors'),
                           ('myomatous','myomatous neoplasms'),
                           ('myxomatous','myxomatous neoplasms'),
                           ('neuroepitheliomatous','neuroepitheliomatous neoplasms'),
                           ('nevi','nevi and melanomas'),
                           ('paragangliomas','paragangliomas and glumus tumors'),
                           ('soft','soft tissue tumors and sarcomas, NOS'),
                           ('squamous','squamous cell neoplasms'),
                           ('synovial','synovial-like neoplasms'),
                           ('transitional','transitional cell papillomas and carcinomas'),
                           ('unspecified','unspecified neoplasms'),
                           ('not','None of the above')],
                       validators=[Required()])


    laterality = SelectField('Laterality', default='0',
        choices = [
                   ('left','left: origin of primary'),
                   ('not','not a paired site'),
                   ('only','only one side involved, right or left origin unspecified'),
                   ('paired','paired site, but no information concerning laterality; midline tumor'),
                   ('right','right: origin of primary'),
                   ('not','None of the above')],
                    validators=[Required()])


    maritalstatus = SelectField('Marital Status at Dx', default='0',
      choices = [('divorced','Divorced'),
                 ('married','Married including common law'),
                 ('separated','Separated'),
                ('single','Single ,never married'),
                 ('unknown','Unknown'),
                 ('unmarried','Unmarried or domestic partner'),
                 ('widowed','Widowed')],
                  validators=[Required()])

            


    monthofdiagnosis = SelectField('Month of Diagnosis', default='0',
        choices = [('jan','Jan'),
                   ('feb','Feb'),
                   ('mar','Mar'),
                   ('apr','Apr'),
                   ('may','May'),
                   ('jun','Jun'),
                   ('jul','Jul'),
                   ('aug','Aug'),
                   ('sep','Sep'),
                   ('oct','Oct'),
                   ('nov','Nov'),
                   ('dec','Dec')],
            validators=[Required()])


    numberofprimaries = FloatField('How many primaries?', validators=[Required()])


    raceethnicity = SelectField('Race_ethnicity', default='0',
        choices = [('americanindian','American Indian, Aleutian, Alaskan Native or Eskimo'),
                   ('asianindian','Asian Indian'),
                   ('asianindianpakistani','Asian Indian or Pakistani'),
                   ('black','Black'),
                   ('chinese','Chinese'),
                   ('fijiislander','Fiji Islander'),
                   ('filipino','Filipino'),
                   ('guamanian','Guamanian'),
                   ('hawaiian','Hawaiian'),
                   ('hmong','Hmong'),
                   ('japanese','Japanese'),
                   ('kampuchean','Kampuchean'),
                   ('korean','Korean'),
                   ('laotian','Laotian'),
                   ('melanesian','Melanesian'),
                   ('micronesian','Micronesian'),
                   ('newguinean','New Guinean'),
                   ('other','Other'),
                   ('otherasian','Other Asian'),
                   ('pacific','Pacific Islander'),
                   ('pakistani','Pakistani'),
                   ('polynesian','Polynesian'),
                   ('samoan','Samoan'),
                   ('thai','Thai'),
                   ('tongan','Tongan'),
                   ('unknown','Unknown'),
                   ('vietnamese','Vietnamese'),
                   ('white','White')],
            validators=[Required()])


    


                   


    seerhistoric = SelectField('seer_historic_stage_a', default='0',
        choices = [('distant','Distant'),
                   ('in','In situ'),
                   ('localized','Localized'),
                   ('regional','Regional'),
                   ('unstaged','Unstaged')],
            validators=[Required()])


    sex = SelectField('Gender', default='0',
        choices = [('male','Male'),
                   ('female','Female')],
            validators=[Required()])



    spanish = SelectField('spanish_hispanic_origin', default='0',
        choices = [('cuban','Cuban'),
                   ('dominican','Dominican Republic'),
                   ('mexican','Mexican'),
                   ('nonspanish','Non-Spanish/Non-hispanic'),
                   ('other','Other specified Spanish/Hispanic origin (excludes Dominican Republic)'),
                   ('puerto','Puerto Rican'),
                   ('south','South or Central American (except Brazil)'),
                   ('surname','Spanish surname only'),
                   ('nos','Spanish, NOS; Hispanic, NOS; Latino NOS'),
                   ('unknown','Unknown whether Spanish/Hispanic or not')],
            validators=[Required()])

    
    yob = SelectField('Year of Birth',
                      choices = yoblistchoices, 
                      validators=[Required()])


    yod = SelectField('Year of Diagnosis',
                      choices = yodlistchoices,
                      validators=[Required()])
    

    
    
    submit = SubmitField('Submit')




class LastNameForm(Form):
    lastname = StringField('What is your last name?', validators=[Required()])
    

    


app = Flask(__name__)

#manager = Manager(app)


app.config['SECRET_KEY'] = 'hard to guess string'




bootstrap = Bootstrap(app)
moment = Moment(app)


clf = joblib.load('COLONCLASSIFIER/rfcolon.pkl')



def get_survival_function(document):
    """takes the input of the text area field and
    returns the survival function values at 6 months, 
    12 months and 60 months."""
    X = document
    print X
    A = []
    p_so_far = 1
    for i in range(108):
        p_cur = clf.predict_proba(np.append(X, i))[0][1]
        A.append(p_so_far * p_cur)
        p_so_far = p_so_far*(1 - p_cur)
    As = pd.Series(A)
    Asurv = 1 - As.cumsum()
    prob6 = Asurv.loc[6]
    prob12 = Asurv.loc[12]
    prob60 = Asurv.loc[60]
    return prob6, prob12, prob60, Asurv




def get_one_group(acdf,numberofsubjects):
    """Returns a pandas series"""
    import random
    a = list()
    for i in range(numberofsubjects):
        try:
            b = get_month_from_cdf(acdf)
            a.append(b)
        except:
            pass
    c = pd.Series(a)
    return c



def get_lat_lng_elevation(address):
    """takes an address like the values in 
    df_fips_codes_website['address'], queries two different 
    google maps apis and returns the corresonding lat, lng, and
    elevation of the address. In the case of county level addresses,
    the returned point corresponds to the middle of the county"""
    import re, json, urllib
    
    
    # first get the lat long and make sure the address is of the correct form
    
    prelatlng = "https://maps.googleapis.com/maps/api/geocode/json?address="
    newaddress = re.sub(r"\s+", '+', address) 
    newaddress = re.sub(r"\xf1a", "n", newaddress)
    print newaddress
    postlatlng = "&key=AIzaSyDEVzo20hSeLcu1bSDUohZrjBTrWkdke18"
    
    latlngurl = prelatlng + newaddress + postlatlng
    
    responselatlng = urllib2.urlopen(latlngurl)
    htmllatlng = responselatlng.read()
    thinglatlng = json.loads(htmllatlng)
    lat = thinglatlng["results"][0]["geometry"]["location"]["lat"]
    lng = thinglatlng["results"][0]["geometry"]["location"]["lng"]
    
    
    # now get the corresponding elevation
    
    preelevation = "https://maps.googleapis.com/maps/api/elevation/json?locations="
    middleurl = str(lat) + ',' + str(lng)
    postelevation = "&key=AIzaSyDEVzo20hSeLcu1bSDUohZrjBTrWkdke18"
    
    elevationurl = preelevation + middleurl + postelevation
    
    responseelevation = urllib2.urlopen(elevationurl)
    htmlelevation = responseelevation.read()
    thingelevation = json.loads(htmlelevation)
    
    elevation_meters = thingelevation["results"][0]["elevation"]
    
    # the returned elevation is in meters. lets use feet .
    # the metric system is for assholes
    
    elevation_feet = elevation_meters * 3.28084
    
    print address, lat, lng, elevation_feet
    return address, lat, lng, elevation_feet
    


def run_server():
    port = int(os.environ.get("PORT", 5000))
    http_server = tornado.httpserver.HTTPServer(
        tornado.wsgi.WSGIContainer(app)
    )
    # http_server.listen(5000)
    http_server.listen(port)
    # Reads args given at command line (this also enables logging to stderr)
    tornado.options.parse_command_line()

    # Start the I/O loop with autoreload
    io_loop = tornado.ioloop.IOLoop.instance()
    tornado.autoreload.start(io_loop)
    try:
        io_loop.start()
    except KeyboardInterrupt:
        pass



@app.route('/')
def index():
    form = NameForm(request.form)
    return render_template('reviewform.html', form=form)







@app.route('/results', methods=['POST'])
def results():
    form = NameForm(request.form)
    session['labels'] = [str(a) for a in range(120)]
    if request.method == 'POST' and form.validate_on_submit():
                
        session['yob'] = form.yob.data
        session['yod'] = form.yod.data
                   
            
        yobgood = int(session['yob'])
        print yobgood, type(yobgood)
        print session['yob'], type(session['yob'])
        
        session['cs_tumor_size'] = form.cs_tumor_size.data
        
        print session['cs_tumor_size']
        session['address'] = form.address.data
        print session['address'], type(session['address'])
        newaddress, lat, lng, elevation_feet = get_lat_lng_elevation(str(session['address']))
        print newaddress, lat, lng, elevation_feet
        session['lat'] = lat
        session['lng'] = lng
        session['elevation'] = elevation_feet

        session['number_of_primaries'] = form.numberofprimaries.data

        
                            
                        

        session['grade'] = form.grade.data

        if form.grade.data == 'ce':
            session['grade_ce'] = '1'
        else:
            session['grade_ce'] = '0'

        
        if form.grade.data == 'mo':
            session['grade_mo'] = '1'
        else:
            session['grade_mo'] = '0'

        if form.grade.data == 'po':
            session['grade_po'] = '1'
        else:
            session['grade_po'] = '0'


        if form.grade.data == 'un':
            session['grade_un'] = '1'
        else:
            session['grade_un'] = '0'

        if form.grade.data == 'we':
            session['grade_we'] = '1'
        else:
            session['grade_we'] = '0'

        if form.hist.data == 'acinar':
            session['hist_acinar'] = '1'
        else:
            session['hist_acinar'] = '0'

            
        if form.hist.data == 'adenomas':
            session['hist_adenomas'] = '1'
        else:
            session['hist_adenomas'] = '0'

        if form.hist.data == 'blood':
            session['hist_blood'] = '1'
        else:
            session['hist_blood'] = '0'

        if form.hist.data == 'complex_epithelial':
            session['hist_complex_epithelial'] = '1'
        else:
            session['hist_complex_epithelial'] = '0'


        if form.hist.data == 'complex_mixed':
            session['hist_complex_mixed'] = '1'
        else:
            session['hist_complex_mixed'] = '0'
            

        if form.hist.data == 'cystic':
            session['hist_cystic'] = '1'
        else:
            session['hist_cystic'] = '0'

        if form.hist.data == 'ductal':
            session['hist_ductal'] = '1'
        else:
            session['hist_ductal'] = '0'


        if form.hist.data == 'epithelial':
            session['hist_epithelial'] = '1'
        else:
            session['hist_epithelial'] = '0'

                           

        if form.hist.data == 'fibromatuos':
            session['hist_fibromatuos'] = '1'
        else:
            session['hist_fibromatuos'] = '0'

        if form.hist.data == 'germ':
            session['hist_germ'] = '1'
        else:
            session['hist_germ'] = '0'



        

        if form.hist.data == 'lipomatous':
            session['hist_lipomatous'] = '1'
        else:
            session['hist_lipomatous'] = '0'

        if form.hist.data == 'misc_bone':
            session['hist_misc_bone'] = '1'
        else:
            session['hist_misc_bone'] = '0'

        

        

        if form.hist.data == 'myomatous':
            session['hist_myomatous'] = '1'
        else:
            session['hist_myomatous'] = '0'


        
            
        

        if form.hist.data == 'neuroepitheliomatous':
            session['hist_neuroepitheliomatous'] = '1'
        else:
            session['hist_neuroepitheliomatous'] = '0'

        if form.hist.data == 'nevi':
            session['hist_nevi'] = '1'
        else:
            session['hist_nevi'] = '0'


        

        if form.hist.data == 'paragangliomas':
            session['hist_paragangliomas'] = '1'
        else:
            session['hist_paragangliomas'] = '0'


        if form.hist.data == 'soft':
            session['hist_soft'] = '1'
        else:
            session['hist_soft'] = '0'


        if form.hist.data == 'squamous':
            session['hist_squamous'] = '1'
        else:
            session['hist_squamous'] = '0'

        if form.hist.data == 'synovial':
            session['hist_synovial'] = '1'
        else:
            session['hist_synovial'] = '0'

        

        if form.hist.data == 'transitional':
            session['hist_transitional'] = '1'
        else:
            session['hist_transitional'] = '0'

        


        if form.hist.data == 'unspecified':
            session['hist_unspecified'] = '1'
        else:
            session['hist_unspecified'] = '0'

        if form.hist.data == 'not':
            session['hist_not'] = '1'
        else:
            session['hist_not'] = '0'



        


        if form.laterality.data == 'left':
            session['laterality_left'] = '1'
        else:
            session['laterality_left'] = '0'

        if form.laterality.data == 'not':
            session['laterality_not'] = '1'
        else:
            session['laterality_not'] = '0'

        if form.laterality.data == 'only':
            session['laterality_only'] = '1'
        else:
            session['laterality_only'] = '0'

        if form.laterality.data == 'paired':
            session['laterality_paired'] = '1'
        else:
            session['laterality_paired'] = '0'

        if form.laterality.data == 'right':
            session['laterality_right'] = '1'
        else:
            session['laterality_right'] = '0'
            

        if form.maritalstatus.data == 'divorced':
            session['maritalstatus_divorced'] = '1'
        else:
            session['maritalstatus_divorced'] = '0'


        if form.maritalstatus.data == 'married':
            session['maritalstatus_married'] = '1'
        else:
            session['maritalstatus_married'] = '0'


        if form.maritalstatus.data == 'separated':
            session['maritalstatus_separated'] = '1'
        else:
            session['maritalstatus_separated'] = '0'
            


        if form.maritalstatus.data == 'single':
            session['maritalstatus_single'] = '1'
        else:
            session['maritalstatus_single'] = '0'


        if form.maritalstatus.data == 'unknown':
            session['maritalstatus_unknown'] = '1'
        else:
            session['maritalstatus_unknown'] = '0'


        if form.maritalstatus.data == 'unmarried':
            session['maritalstatus_unmarried'] = '1'
        else:
            session['maritalstatus_unmarried'] = '0'


        if form.maritalstatus.data == 'widowed':
            session['maritalstatus_widowed'] = '1'
        else:
            session['maritalstatus_widowed'] = '0'



        if form.monthofdiagnosis.data == 'jan':
            session['monthofdiagnosis_jan'] = '1'
        else:
            session['monthofdiagnosis_jan'] = '0'


        


        if form.monthofdiagnosis.data == 'feb':
            session['monthofdiagnosis_feb'] = '1'
        else:
            session['monthofdiagnosis_feb'] = '0'


        if form.monthofdiagnosis.data == 'mar':
            session['monthofdiagnosis_mar'] = '1'
        else:
            session['monthofdiagnosis_mar'] = '0'


        if form.monthofdiagnosis.data == 'apr':
            session['monthofdiagnosis_apr'] = '1'
        else:
            session['monthofdiagnosis_apr'] = '0'


        if form.monthofdiagnosis.data == 'may':
            session['monthofdiagnosis_may'] = '1'
        else:
            session['monthofdiagnosis_may'] = '0'


        if form.monthofdiagnosis.data == 'jun':
            session['monthofdiagnosis_jun'] = '1'
        else:
            session['monthofdiagnosis_jun'] = '0'


        if form.monthofdiagnosis.data == 'jul':
            session['monthofdiagnosis_jul'] = '1'
        else:
            session['monthofdiagnosis_jul'] = '0'


        if form.monthofdiagnosis.data == 'aug':
            session['monthofdiagnosis_aug'] = '1'
        else:
            session['monthofdiagnosis_aug'] = '0'


        if form.monthofdiagnosis.data == 'sep':
            session['monthofdiagnosis_sep'] = '1'
        else:
            session['monthofdiagnosis_sep'] = '0'

        if form.monthofdiagnosis.data == 'oct':
            session['monthofdiagnosis_oct'] = '1'
        else:
            session['monthofdiagnosis_oct'] = '0'


        if form.monthofdiagnosis.data == 'nov':
            session['monthofdiagnosis_nov'] = '1'
        else:
            session['monthofdiagnosis_nov'] = '0'


        if form.monthofdiagnosis.data == 'dec':
            session['monthofdiagnosis_dec'] = '1'
        else:
            session['monthofdiagnosis_dec'] = '0'



        if form.raceethnicity.data == 'americanindian':
            session['raceethnicity_americanindian'] = '1'
        else:
            session['raceethnicity_americanindian'] = '0'


        if form.raceethnicity.data == 'asianindian':
            session['raceethnicity_asianindian'] = '1'
        else:
            session['raceethnicity_asianindian'] = '0'

        if form.raceethnicity.data == 'asianindianpakistani':
            session['raceethnicity_asianindianpakistani'] = '1'
        else:
            session['raceethnicity_asianindianpakistani'] = '0'

        if form.raceethnicity.data == 'black':
            session['raceethnicity_black'] = '1'
        else:
            session['raceethnicity_black'] = '0'

        


        if form.raceethnicity.data == 'chinese':
            session['raceethnicity_chinese'] = '1'
        else:
            session['raceethnicity_chinese'] = '0'

        if form.raceethnicity.data == 'fijiislander':
            session['raceethnicity_fijiislander'] = '1'
        else:
            session['raceethnicity_fijiislander'] = '0'

        if form.raceethnicity.data == 'filipino':
            session['raceethnicity_filipino'] = '1'
        else:
            session['raceethnicity_filipino'] = '0'

        if form.raceethnicity.data == 'guamanian':
            session['raceethnicity_guamanian'] = '1'
        else:
            session['raceethnicity_guamanian'] = '0'

        if form.raceethnicity.data == 'hawaiian':
            session['raceethnicity_hawaiian'] = '1'
        else:
            session['raceethnicity_hawaiian'] = '0'

        if form.raceethnicity.data == 'hmong':
            session['raceethnicity_hmong'] = '1'
        else:
            session['raceethnicity_hmong'] = '0'

        


        if form.raceethnicity.data == 'japanese':
            session['raceethnicity_japanese'] = '1'
        else:
            session['raceethnicity_japanese'] = '0'

        if form.raceethnicity.data == 'kampuchean':
            session['raceethnicity_kampuchean'] = '1'
        else:
            session['raceethnicity_kampuchean'] = '0'

        if form.raceethnicity.data == 'korean':
            session['raceethnicity_korean'] = '1'
        else:
            session['raceethnicity_korean'] = '0'


        if form.raceethnicity.data == 'laotian':
            session['raceethnicity_laotian'] = '1'
        else:
            session['raceethnicity_laotian'] = '0'


        if form.raceethnicity.data == 'melanesian':
            session['raceethnicity_melanesian'] = '1'
        else:
            session['raceethnicity_melanesian'] = '0'

        if form.raceethnicity.data == 'micronesian':
            session['raceethnicity_micronesian'] = '1'
        else:
            session['raceethnicity_micronesian'] = '0'

        if form.raceethnicity.data == 'newguinean':
            session['raceethnicity_newguinean'] = '1'
        else:
            session['raceethnicity_newguinean'] = '0'


        if form.raceethnicity.data == 'other':
            session['raceethnicity_other'] = '1'
        else:
            session['raceethnicity_other'] = '0'


        if form.raceethnicity.data == 'otherasian':
            session['raceethnicity_otherasian'] = '1'
        else:
            session['raceethnicity_otherasian'] = '0'


        if form.raceethnicity.data == 'pacific':
            session['raceethnicity_pacific'] = '1'
        else:
            session['raceethnicity_pacific'] = '0'

        if form.raceethnicity.data == 'pakistani':
            session['raceethnicity_pakistani'] = '1'
        else:
            session['raceethnicity_pakistani'] = '0'

        if form.raceethnicity.data == 'polynesian':
            session['raceethnicity_polynesian'] = '1'
        else:
            session['raceethnicity_polynesian'] = '0'

        if form.raceethnicity.data == 'samoan':
            session['raceethnicity_samoan'] = '1'
        else:
            session['raceethnicity_samoan'] = '0'


        if form.raceethnicity.data == 'thai':
            session['raceethnicity_thai'] = '1'
        else:
            session['raceethnicity_thai'] = '0'

        if form.raceethnicity.data == 'tongan':
            session['raceethnicity_tongan'] = '1'
        else:
            session['raceethnicity_tongan'] = '0'


        if form.raceethnicity.data == 'unknown':
            session['raceethnicity_unknown'] = '1'
        else:
            session['raceethnicity_unknown'] = '0'


        if form.raceethnicity.data == 'vietnamese':
            session['raceethnicity_vietnamese'] = '1'
        else:
            session['raceethnicity_vietnamese'] = '0'



        if form.raceethnicity.data == 'white':
            session['raceethnicity_white'] = '1'
        else:
            session['raceethnicity_white'] = '0'
        

        



        

        
        


        



        if form.seerhistoric.data == 'distant':
            session['seerhistoric_distant'] = '1'
        else:
            session['seerhistoric_distant'] = '0'


        if form.seerhistoric.data == 'in':
            session['seerhistoric_in'] = '1'
        else:
            session['seerhistoric_in'] = '0'


        if form.seerhistoric.data == 'localized':
            session['seerhistoric_localized'] = '1'
        else:
            session['seerhistoric_localized'] = '0'

        if form.seerhistoric.data == 'regional':
            session['seerhistoric_regional'] = '1'
        else:
            session['seerhistoric_regional'] = '0'


        if form.seerhistoric.data == 'unstaged':
            session['seerhistoric_unstaged'] = '1'
        else:
            session['seerhistoric_unstaged'] = '0'



        if form.sex.data == 'female':
            session['sex_female'] = '1'
        else:
            session['sex_female'] = '0'


        if form.spanish.data == 'cuban':
            session['spanish_cuban'] = '1'
        else:
            session['spanish_cuban'] = '0'

        if form.spanish.data == 'dominican':
            session['spanish_dominican'] = '1'
        else:
            session['spanish_dominican'] = '0'


        if form.spanish.data == 'mexican':
            session['spanish_mexican'] = '1'
        else:
            session['spanish_mexican'] = '0'


        if form.spanish.data == 'nonspanish':
            session['spanish_nonspanish'] = '1'
        else:
            session['spanish_nonspanish'] = '0'

        if form.spanish.data == 'other':
            session['spanish_other'] = '1'
        else:
            session['spanish_other'] = '0'


        if form.spanish.data == 'puerto':
            session['spanish_puerto'] = '1'
        else:
            session['spanish_puerto'] = '0'

        if form.spanish.data == 'south':
            session['spanish_south'] = '1'
        else:
            session['spanish_south'] = '0'



        if form.spanish.data == 'surname':
            session['spanish_surname'] = '1'
        else:
            session['spanish_surname'] = '0'

        if form.spanish.data == 'nos':
            session['spanish_nos'] = '1'
        else:
            session['spanish_nos'] = '0'

        if form.spanish.data == 'unknown':
            session['spanish_unknown'] = '1'
        else:
            session['spanish_unknown'] = '0'
        

                 
        session_data = np.array( [session['cs_tumor_size'],
                                  session['elevation'],
                                  session['grade_ce'],
                                  session['grade_mo'],
                                  session['grade_po'],
                                  session['grade_un'],
                                  session['grade_we'],
                                  session['hist_acinar'],
                                  session['hist_adenomas'],
                                  session['hist_blood'],
                                  session['hist_complex_epithelial'],
                                  session['hist_complex_mixed'],
                                  session['hist_cystic'],
                                  session['hist_ductal'],
                                  session['hist_epithelial'],
                                  session['hist_fibromatuos'],
                                  session['hist_germ'],
                                  session['hist_lipomatous'],
                                  session['hist_misc_bone'],
                                  session['hist_myomatous'],
                                  session['hist_neuroepitheliomatous'],
                                  session['hist_nevi'],
                                  session['hist_paragangliomas'],
                                  session['hist_soft'],
                                  session['hist_squamous'],
                                  session['hist_synovial'],
                                  session['hist_transitional'],
                                  session['hist_unspecified'],
                                  session['lat'],
                                  session['laterality_left'],
                                  session['laterality_not'],
                                  session['laterality_only'],
                                  session['laterality_paired'],
                                  session['laterality_right'],
                                  session['lng'],
                                  session['maritalstatus_divorced'],
                                  session['maritalstatus_married'],
                                  session['maritalstatus_separated'],
                                  session['maritalstatus_single'],
                                  session['maritalstatus_unknown'],
                                  session['maritalstatus_unmarried'],
                                  session['maritalstatus_widowed'],
                                  session['monthofdiagnosis_apr'],
                                  session['monthofdiagnosis_aug'],
                                  session['monthofdiagnosis_dec'],
                                  session['monthofdiagnosis_feb'],
                                  session['monthofdiagnosis_jan'],
                                  session['monthofdiagnosis_jul'],
                                  session['monthofdiagnosis_jun'],
                                  session['monthofdiagnosis_mar'],
                                  session['monthofdiagnosis_may'],
                                  session['monthofdiagnosis_nov'],
                                  session['monthofdiagnosis_oct'],
                                  session['monthofdiagnosis_sep'],
                                  session['number_of_primaries'],
                                  session['raceethnicity_americanindian'],
                                  session['raceethnicity_asianindian'],
                                  session['raceethnicity_asianindianpakistani'],
                                  session['raceethnicity_black'],
                                  session['raceethnicity_chinese'],
                                  session['raceethnicity_fijiislander'],
                                  session['raceethnicity_filipino'],
                                  session['raceethnicity_guamanian'],
                                  session['raceethnicity_hawaiian'],
                                  session['raceethnicity_hmong'],
                                  session['raceethnicity_japanese'],
                                  session['raceethnicity_kampuchean'],
                                  session['raceethnicity_korean'],
                                  session['raceethnicity_laotian'],
                                  session['raceethnicity_melanesian'],
                                  session['raceethnicity_micronesian'],
                                  session['raceethnicity_newguinean'],
                                  session['raceethnicity_other'],
                                  session['raceethnicity_otherasian'],
                                  session['raceethnicity_pacific'],
                                  session['raceethnicity_pakistani'],
                                  session['raceethnicity_polynesian'],
                                  session['raceethnicity_samoan'],
                                  session['raceethnicity_thai'],
                                  session['raceethnicity_tongan'],
                                  session['raceethnicity_unknown'],
                                  session['raceethnicity_vietnamese'],
                                  session['raceethnicity_white'],
                                  session['seerhistoric_distant'],
                                  session['seerhistoric_in'],
                                  session['seerhistoric_localized'],
                                  session['seerhistoric_regional'],
                                  session['seerhistoric_unstaged'],
                                  session['sex_female'],
                                  session['spanish_cuban'],
                                  session['spanish_dominican'],
                                  session['spanish_mexican'],
                                  session['spanish_nonspanish'],
                                  session['spanish_other'],
                                  session['spanish_puerto'],
                                  session['spanish_south'],
                                  session['spanish_surname'],
                                  session['spanish_nos'],
                                  session['spanish_unknown'],
                                  session['yob'],
                                  session['yod']]).astype('float')

        

        print session_data

        labels = [str(a) for a in range(120)]

        print labels

        session['labels'] = [str(a) for a in range(120)]

        print session['labels'], type(session['labels'])

        session_data_string = str(session_data)

        session['datax'] = session_data_string

        session_data_list = list(session_data)

        session['datas'] = session_data_list

        values = session_data_list

        session['values'] = session_data_list

        print values

        print session.get('datax')

        prob6, prob12, prob60, Asurv = get_survival_function(session_data)

        print prob6, prob12, prob60


        datacountscdfdict = {1: 0.053045113481911786, 2: 0.089202926883762496, 3: 0.11724292018097525, 4: 0.13977173285669067,
                         5: 0.16067139585544321, 6: 0.17958815096166378, 7: 0.19792772161090319, 8: 0.21510361391945482,
                         9: 0.23087378279245563, 10: 0.24683944962669196, 11: 0.26265616563332028, 12: 0.27865907017445862,
                         13: 0.29261390083598648, 14: 0.30764862499767259, 15: 0.32232959094378966, 16: 0.33641475357947453,
                         17: 0.3504347502280809, 18: 0.36364482675156856, 19: 0.37746932543893941, 20: 0.39056768884172105,
                         21: 0.40402911988679729,
                         22: 0.41729505297063801, 23: 0.42982554134316403, 24: 0.44132268334915931, 25: 0.45313634586382168,
                         26: 0.46500586493883705, 27: 0.47634474669049881, 28: 0.48808393379135712, 29: 0.49921800815505779,
                         30: 0.50996108659628736, 31: 0.52122549293414511, 32: 0.53126105494423648, 33: 0.54181794485095602,
                         34: 0.55223519335679305, 35: 0.56247556275484556, 36: 0.57196186858813236, 37: 0.58116889161965413,
                         38: 0.59023627325029326, 39: 0.59970396023012906, 40: 0.60844551192537566, 41: 0.61741048986203428,
                         42: 0.62594723416931985, 43: 0.63477257070509596, 44: 0.64289039080973387, 45: 0.65185536874639249,
                         46: 0.66095067865720813, 47: 0.66920814016272867, 48: 0.67723286600011157, 49: 0.68501554674263143,
                         50: 0.69237930328250374, 51: 0.70048781396041615, 52: 0.70832635126328902, 53: 0.71580182092386735,
                         54: 0.72292353236887652, 55: 0.73047347744325886, 56: 0.73754864175464052, 57: 0.74493101714796384,
                         58: 0.75237855852836566, 59: 0.75953750768027684, 60: 0.76686402651324714, 61: 0.77218901860023448,
                         62: 0.7789569718296746, 63: 0.78533392913664368, 64: 0.79176674300396577, 65: 0.79832988884544487,
                         66: 0.80420413710923677, 67: 0.81062764154983336, 68: 0.81646465210672325, 69: 0.82292539425422184,
                         70: 0.82879033309128824, 71: 0.83461803422145264, 72: 0.84025954681710702, 73: 0.84533318438250571,
                         74: 0.8511143383790426, 75: 0.85584352715559775, 76: 0.86080545160029043, 77: 0.86577668547170861,
                         78: 0.87076653819657779, 79: 0.87603567372321201, 80: 0.88117447727568921, 81: 0.88650877878940204,
                         82: 0.89161965406170274, 83: 0.89684224245470945, 84: 0.90137593327002907, 85: 0.90582583924481919,
                         86: 0.91052709974119783, 87: 0.91507009998324296, 88: 0.91987376417360212, 89: 0.92430505129494123,
                         90: 0.92862462529557421, 91: 0.93305591241691332, 92: 0.93783164832709598, 93: 0.9423187920087881,
                         94: 0.94686179225083322, 95: 0.9510882719842112, 96: 0.95512856318307915, 97: 0.95901990355433908,
                         98: 0.9628088402316185, 99: 0.96661639576234892, 100: 0.97061013982758937, 101: 0.9744828613453983,
                         102: 0.97821594146232471, 103: 0.98225623266119266, 104: 0.9861848107393546, 105: 0.9898527248692025,
                         106: 0.99366028039993293, 107: 0.99693719860730967, 108: 0.99999999999999989}

        datacountscdf = pd.Series(datacountscdfdict)

        basecdf = -Asurv + 1

        print basecdf

        print datacountscdf


        def get_month_from_cdf(acdf):
            import random
            pval = random.uniform(0,100)/100.0
            #print(pval)
            if (pval <= acdf.max() + .001): 
                try:
                    return acdf[acdf <= pval].tail(1).index[0]
                except:
                    return 0
            else:
                return len(basecdf) 



        def get_one_group(acdf,numberofsubjects):
            """Returns a pandas series"""
            import random
            a = list()
            for i in range(numberofsubjects):
                try:
                    b = get_month_from_cdf(acdf)
                    a.append(b)
                except:
                    pass
            c = pd.Series(a)
            return c
            
        
        listofcurves = list()
        listofcurves.append(Asurv)


        for i in range(800):
            import random 
            numberofsubjects = get_month_from_cdf(datacountscdf) + 1
            samp1 = get_one_group(basecdf, numberofsubjects)
            samp1pmf = samp1.value_counts(normalize=True).sort_index()
            samp1cdf = samp1pmf.cumsum()
            samp1st = -samp1cdf + 1
            listofcurves.append(samp1st)
        
        
        dfhuh = pd.DataFrame.from_records(listofcurves)

        print dfhuh.shape
        
        upper = list(dfhuh.quantile(.975).values)
        lower = list(dfhuh.quantile(.025).values)
        print dfhuh.quantile(.975)
        print dfhuh.head()

        

        session['prob6'] = round(prob6,3)
        session['prob12'] = round(prob12,3)
        session['prob60'] = round(prob60,3)
        session['Asurv'] = [round(elem,3) for elem in Asurv]
        session['upper'] = [round(elem,3) for elem in dfhuh.quantile(.975)[:-1]]
        session['lower'] = [round(elem,3) for elem in dfhuh.quantile(.025)[:-1]]
        return render_template('results.html',
                               prob6 = session.get('prob6'),
                               prob12 = session.get('prob12'),
                               prob60 = session.get('prob60'),
                               values = session.get('Asurv'),
                               upper = session.get('upper'),
                               lower = session.get('lower'),
                                labels= ['0','','','','','','','','','',
                                    '10','','','','','','','','','',
                                    '20','','','','','','','','','',
                                    '30','','','','','','','','','',
                                    '40','','','','','','','','','',
                                    '50','','','','','','','','','',
                                    '60','','','','','','','','','',
                                    '70','','','','','','','','','',
                                    '80','','','','','','','','','',
                                    '90','','','','','','','','','',
                                    '100','','','','','','','107'])
                               
                            

    
    
    return render_template('reviewform.html',
                           form = form)



#@app.route('/user/<id>')
#def get_user(id):
#    user = str(id)
#    if user != 'Tom Brady':
#        abort(404)
#    return '<h1>Hello, %s</h1>' % 'Tom Brady'


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(505)
def internal_server_error(e):
    return render_template('500.html'), 500



        








if __name__ == '__main__':
   run_server()
   #app.run(debug=True)



