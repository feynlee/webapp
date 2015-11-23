from flask import Flask, render_template, request, redirect
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.palettes import Spectral11
import requests
import simplejson as json
import pandas as pd
import Quandl

app = Flask(__name__)

select={}



@app.route('/')
def main():
  return redirect('/index')

@app.route('/index',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        r=request.form
        # app.vars['ticker']=request.form['ticker_name']
        stock=request.form['ticker_name']

        options=['Close','Adj. Close','Open','Adj. Open']
        for item in options:
            if item in request.form:
                continue
            else:
                options.remove(item)



        api_key = 'yhxmmVTWyYhsYwjwQdjx'
        mydata = Quandl.get('WIKI/'+stock, authtoken= api_key)

        plot = figure(
              # tools=TOOLS,
              title='Data from Quandle WIKI set',
              x_axis_label='date',
              x_axis_type='datetime')

        # numlines = len(options)
        # colors=[]
        options=['Open','Close','Adj. Open','Adj. Close']
        colorselect = dict([('Close','blue'),('Adj. Close','green'),('Open','orange'),('Adj. Open','red')])
        # for item in options:
        #     colors.append(colorselect[item])
        #
        for item in options:
            plot.line(x=mydata.index.tolist(), y=mydata[item], line_color = colorselect[item], legend = item)

        # item='Open'
        # plot.line(x=mydata.index.tolist(), y=mydata[item],line_color='red')
        print(request.form)
        print(item)


        # plot.line(pd_combined['Date'].tolist(), pd_combined['Open'].tolist(), line_color='red')
        # plot.multi_line(xs=[[1,2,3]], ys=[[3,4,8]],color=['red'])
        # plot.line([1,2,3], [3,4,8],line_color=['red'])



        # app.vars['Open']=request.form['Open']
        # app.vars['Close']=request.form['Close']
        # app.vars['Adj_Open']=request.form['Adj. Open']
        # app.vars['Adj_Close']=request.form['Adj. Close']

        # print(json_object)


        # f = open('data.txt','w')
        # f.write('tiker: %s\n%s\n%s\n%s\n%s\n'%(app.vars['ticker'],app.vars['Open'],app.vars['Close'],app.vars['Adj_Open'],app.vars['Adj_Close']))
        # f.close()

        script, div = components(plot)
        return render_template('graph.html', script=script, div=div)
        # return 'request.method was not a GET!'

# @app.route('/graph',methods=['GET','POST'])
# def index():
#     if request.method == 'GET':
#         return render_template('index.html')
#     else:
#         app.vars['ticker']=request.form['ticker_name']
#         f = open('data.txt','w')
#         f.write('tiker: %s/n'%app.vars['ticker'])

if __name__ == '__main__':
    # app.run(debug=True)
  app.run(port=33507)