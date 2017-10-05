from django.shortcuts import render, redirect
from.models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from forms import SignUpForm
from django.template.loader import get_template
from forms import ManufactureForm
from datetime import date
import bt
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

# Create your views here.

@login_required(login_url="/")
def home(request):
    
    if request.method=='POST':
        form = ManufactureForm(request.POST)
        print date.today
        print request.POST.get('start_date')
        #print form
        #print start_date
        if form.is_valid():
            form.save()
            start_date = form.cleaned_data.get('start_date')

            end_date = form.cleaned_data.get('end_date')
            warehouse1= form.cleaned_data.get('warehouse1')
            store1= form.cleaned_data.get('store1')
            warehouse2= form.cleaned_data.get('warehouse2')
            store2= form.cleaned_data.get('store1')
            warehouse3= form.cleaned_data.get('warehouse3')
            store3= form.cleaned_data.get('store3')
            warehouse4= form.cleaned_data.get('warehouse4')
            store4= form.cleaned_data.get('store4')
            warehouse5= form.cleaned_data.get('warehouse5')
            store5= form.cleaned_data.get('store5')
            warehouse6= form.cleaned_data.get('warehouse6')
            store6= form.cleaned_data.get('store6')
            warehouse7= form.cleaned_data.get('warehouse7')
            store7= form.cleaned_data.get('store7')
            warehouse8= form.cleaned_data.get('warehouse8')
            store8= form.cleaned_data.get('store8')
            warehouse9= form.cleaned_data.get('warehouse9')
            store9= form.cleaned_data.get('store9')
            warehouse10= form.cleaned_data.get('warehouse10')
            store10= form.cleaned_data.get('store10')
            warehouse11= form.cleaned_data.get('warehouse11')
            store11= form.cleaned_data.get('store11')
            warehouse12= form.cleaned_data.get('warehouse12')
            store12= form.cleaned_data.get('store12')
            warehouse13= form.cleaned_data.get('warehouse13')
            store13= form.cleaned_data.get('store13')
            warehouse14= form.cleaned_data.get('warehouse14')
            store14= form.cleaned_data.get('store14')
            warehouse15= form.cleaned_data.get('warehouse15')
            store15= form.cleaned_data.get('store15')
            like = form.cleaned_data.get('like')
            if like == 'select1':
                weather_all(request)
            if like == 'select2':
                weather_agg(request)
                

                    #return render_to_response('verinc/template.html', {'form' : form,},context_instance=RequestContext(request))

            return redirect('dashboard:home')

    else:
        form = ManufactureForm()
            
    
    return render(request, 'main/home.html', {'form':form})

def urmila(a, name='urmila'):
    print "hi"
    print datetime.now
    start= a.POST.get('start_date')
    start = datetime.strptime(str(start), '%Y-%m-%d')
    print start
    end = a.POST.get('end_date')
    end = datetime.strptime(str(end), '%Y-%m-%d')
    print end
    l = []
    if(a.POST.get('warehouse1')):
        ticker1 = str(a.POST.get('warehouse1'))
        l.append(ticker1)
    if(a.POST.get('warehouse2')):
        ticker2 = str(a.POST.get('warehouse2'))
        l.append(ticker2)
    if(a.POST.get('warehouse3')):
        ticker3 = str(a.POST.get('warehouse3'))
        l.append(ticker3)
    if(a.POST.get('warehouse4')):
        ticker4 = str(a.POST.get('warehouse4'))
        l.append(ticker4)
    if(a.POST.get('warehouse5')):
        ticker5 = str(a.POST.get('warehouse5'))
        l.append(ticker5)
    if(a.POST.get('warehouse6')):
        ticker6 = str(a.POST.get('warehouse6'))
        l.append(ticker6)
    if(a.POST.get('warehouse7')):
        ticker7 = str(a.POST.get('warehouse7'))
        l.append(ticker7)
    if(a.POST.get('warehouse8')):
        ticker8 = str(a.POST.get('warehouse8'))
        l.append(ticker8)
    if(a.POST.get('warehouse9')):
        ticker9 = str(a.POST.get('warehouse9'))
        l.append(ticker9)
    if(a.POST.get('warehouse10')):
        ticker10 = str(a.POST.get('warehouse10'))
        l.append(ticker10)
    if(a.POST.get('warehouse11')):
        ticker11 = str(a.POST.get('warehouse11'))
        l.append(ticker11)
    if(a.POST.get('warehouse12')):
        ticker12 = str(a.POST.get('warehouse12'))
        l.append(ticker12)
    if(a.POST.get('warehouse13')):
        ticker13 = str(a.POST.get('warehouse13'))
        l.append(ticker13)
    if(a.POST.get('warehouse14')):
        ticker14 = str(a.POST.get('warehouse14'))
        l.append(ticker14)
    if(a.POST.get('warehouse15')):
        ticker15 = str(a.POST.get('warehouse15'))
        l.append(ticker15)
    print l
    ticker = l
    data = bt.get(ticker, start=start, end=end)
    print data.head()
    data = data.asfreq(freq='M', method='pad')
    EntryAlgorithm = data.ewm(span=6).mean()
    ExitAlgorithm = data.ewm(span=12).mean()
    tw= EntryAlgorithm.copy()
    tw[EntryAlgorithm>ExitAlgorithm]= 1.0
    tw[EntryAlgorithm<=ExitAlgorithm]= 0.0
    s = bt.Strategy('s1', [bt.algos.RunMonthly(),
                       bt.algos.SelectAll(),
                       bt.algos.WeighTarget(tw),
                       bt.algos.Rebalance()])

    print "uuuuuuuu",s
    test = bt.Backtest(s, data)
    print "oooooo",test
    res = bt.run(test)
    res.plot()
    res.display()
    return True

def allweather(ticker, start, end, name):
    data = bt.get(ticker, start=start, end=end)
    print data.head()
    data = data.asfreq(freq='M', method='pad')
    EntryAlgorithm = data.ewm(span=6).mean()
    ExitAlgorithm = data.ewm(span=12).mean()
  
   
    tw= EntryAlgorithm.copy()
    tw[EntryAlgorithm>ExitAlgorithm]= 1.0
    tw[EntryAlgorithm<=ExitAlgorithm]= 0.0

    s = bt.Strategy(name, [bt.algos.WeighTarget(tw),
                                  bt.algos.RunMonthly(),
                                  bt.algos.Rebalance()], [ticker])
    return bt.Backtest(s, data)

def weather_all(a):
    start= a.POST.get('start_date')
    start = datetime.strptime(str(start), '%Y-%m-%d')
    print start
    end = a.POST.get('end_date')
    end = datetime.strptime(str(end), '%Y-%m-%d')
    print end
    weights = {}
    if(a.POST.get('warehouse1')):
        ticker1 = str(a.POST.get('warehouse1'))
        print ticker1
        asset1 = allweather(ticker1, start, end, name='asset1')
        print asset1 
        t1 = bt.run(asset1)
        # merge1 = t1.data
        # data = bt.merge(merge1)
        w1 = float(a.POST.get('store1'))
        weights['asset1'] = w1
        print w1 
    if(a.POST.get('warehouse2')):
        ticker2 = str(a.POST.get('warehouse2'))
        asset2 = allweather(ticker2, start, end, name='asset2')
        t2 = bt.run(asset2)
        # merge2 = t2.data
        # data = bt.merge(merge2) 
        w2 = float(a.POST.get('store2'))
        weights['asset2'] = w2
        print w2
    if(a.POST.get('warehouse3')):
        ticker3 = str(a.POST.get('warehouse3'))
        asset3 = allweather(ticker3, start, end, name='asset3')
        t3 = bt.run(asset3)
        # merge3 = t3.data
        # data = bt.merge(merge3)
        w3 = float(a.POST.get('store3'))
        weights['asset3'] = w3
        print w3
    if(a.POST.get('warehouse4')):
        ticker4 = str(a.POST.get('warehouse4'))
        asset4 = allweather(ticker4, start, end, name='asset4')
        t4 = bt.run(asset4)
        # merge4 = t4.data
        # data = bt.merge(merge4)
        w4 = float(a.POST.get('store4'))
        weights['asset4'] = w4
        print w4
    if(a.POST.get('warehouse5')):
        ticker5 = str(a.POST.get('warehouse5'))
        asset5 = allweather(ticker5, start, end, name='asset5')
        t5 = bt.run(asset5)
        # merge1 = t5.data
        # data = bt.merge(merge5)
        w5 = float(a.POST.get('store5'))
        weights['asset5'] = w5
        print w5
    if(a.POST.get('warehouse6')):
        ticker6 = str(a.POST.get('warehouse6'))
        asset6 = allweather(ticker6, start, end, name='asset6')
        t6 = bt.run(asset6)
        # merge6 = t6.data
        # data = bt.merge(merge6)
        w6 = float(a.POST.get('store5'))
        weights['asset6'] = w6
        print w6
    if(a.POST.get('warehouse7')):
        ticker7 = str(a.POST.get('warehouse7'))
        asset7 = allweather(ticker7, start, end, name='asset7')
        t7 = bt.run(asset7)
        # merge7 = t1.data
        # data = bt.merge(merge7)
        w7 = float(a.POST.get('store7'))
        weights['asset7'] = w7
        print w7
    if(a.POST.get('warehouse8')):
        ticker8 = str(a.POST.get('warehouse8'))
        asset8 = allweather(ticker8, start, end, name='asset8')
        t8 = bt.run(asset8)
        # merge8 = t8.data
        # data = bt.merge(merge8)
        w8 = float(a.POST.get('store8'))
        weights['asset8'] = w8
        print w8
    if(a.POST.get('warehouse9')):
        ticker9 = str(a.POST.get('warehouse9'))
        asset9 = allweather(ticker9, start, end, name='asset9')
        t9 = bt.run(asset9)
        # merge9 = t9.data
        # data = bt.merge(merge9)
        w9 = float(a.POST.get('store9'))
        weights['asset9'] = w9
        print w9
    if(a.POST.get('warehouse10')):
        ticker10 = str(a.POST.get('warehouse10'))
        asset10 = allweather(ticker10, start, end, name='asset10')
        t10 = bt.run(asset10)
        # merge10 = t10.data
        # data = bt.merge(merge10)
        w10 = float(a.POST.get('store10'))
        weights['asset10'] = w10
        print w10
    if(a.POST.get('warehouse11')):
        ticker11 = str(a.POST.get('warehouse11'))
        asset11 = allweather(ticker11, start, end, name='asset11')
        t11 = bt.run(asset11)
        # merge11 = t11.data
        # data = bt.merge(merge11)
        w11 = float(a.POST.get('store11'))
        weights['asset11'] = w11
        print w11
    if(a.POST.get('warehouse12')):
        ticker12 = str(a.POST.get('warehouse12'))
        asset12 = allweather(ticker12, start, end, name='asset12')
        t12 = bt.run(asset12)
        # merge12 = t12.data
        # data = bt.merge(merge12)
        w12 = float(a.POST.get('store12'))
        weights['asset5'] = w12
        print w12
    if(a.POST.get('warehouse13')):
        ticker13 = str(a.POST.get('warehouse13'))
        asset13 = allweather(ticker13, start, end, name='asset13')
        t13 = bt.run(asset13)
        # merge13 = t13.data
        # data = bt.merge(merge13)
        w13 = float(a.POST.get('store13'))
        weights['asset13'] = w13
        print w13
    if(a.POST.get('warehouse14')):
        ticker14 = str(a.POST.get('warehouse14'))
        asset14 = allweather(ticker14, start, end, name='asset14')
        t14 = bt.run(asset14)
        # merge14 = t14.data
        # data = bt.merge(merge14)
        w14 = float(a.POST.get('store14'))
        weights['asset14'] = w14
        print w14
    if(a.POST.get('warehouse15')):
        ticker15 = str(a.POST.get('warehouse15'))
        asset15 = allweather(ticker14, start, end, name='asset15')
        t15 = bt.run(asset15)
        # merge15 = t15.data
        # data = bt.merge(merge15)
        w15 = float(a.POST.get('store15'))
        weights['asset15'] = w15
        print w15
    
    data = bt.merge(t1['asset1'].prices, t2['asset2'].prices)
    print weights
    print type(data)
   
    s = bt.Strategy('s', [bt.algos.SelectAll(), bt.algos.WeighSpecified(**weights),bt.algos.Rebalance()])
    print "uuuuu", s
    t = bt.Backtest(s, data)
    print "oooooo",t
    res = bt.run(t)
    print res
    
    fig = plt.figure(figsize = (15, 5))
    ax = fig.add_subplot(111)
    ax.plot([1,2,3,4], [10,20,30,40], color='lightblue', linewidth=3)
    plt.show()
    # plt.bar(range(len(res)), res.values(), align='center')
    # plt.xticks(range(len(res)), res.keys())
    # plt.show()



    
    res.display()




def aggressive(ticker, start, end, name):
    data = bt.get(ticker, start=start, end=end)
    print data.head()
    data = data.asfreq(freq='M', method='pad')
    EntryAlgorithm = data.ewm(span=6).mean()
    ExitAlgorithm = data.ewm(span=12).mean()
  
   
    tw= EntryAlgorithm.copy()
    tw[EntryAlgorithm>ExitAlgorithm]= 1.0
    tw[EntryAlgorithm<=ExitAlgorithm]= 0.0

    s = bt.Strategy(name, [bt.algos.RunMonthly(),
                       bt.algos.SelectAll(),
                       bt.algos.WeighEqually(),
                       bt.algos.Rebalance()], [ticker])
    return bt.Backtest(s, data)

def weather_agg(a):
    start= a.POST.get('start_date')
    start = datetime.strptime(str(start), '%Y-%m-%d')
    print start
    end = a.POST.get('end_date')
    end = datetime.strptime(str(end), '%Y-%m-%d')
    print end
    weights = {}
    if(a.POST.get('warehouse1')):
        ticker1 = str(a.POST.get('warehouse1'))
        asset1 = aggressive(ticker1, start, end, name='asset1')
        t1 = bt.run(asset1)
        # merge1 = t1.data
        # data = bt.merge(merge1)
        w1 = float(a.POST.get('store1'))
        weights['asset1'] = w1
        print w1 
    if(a.POST.get('warehouse2')):
        ticker2 = str(a.POST.get('warehouse2'))
        asset2 = aggressive(ticker2, start, end, name='asset2')
        t2 = bt.run(asset2)
        # merge2 = t2.data
        # data = bt.merge(merge2) 
        w2 = float(a.POST.get('store2'))
        weights['asset2'] = w2
        print w2
    if(a.POST.get('warehouse3')):
        ticker3 = str(a.POST.get('warehouse3'))
        asset3 = aggressive(ticker3, start, end, name='asset3')
        t3 = bt.run(asset3)
        # merge3 = t3.data
        # data = bt.merge(merge3)
        w3 = float(a.POST.get('store3'))
        weights['asset3'] = w3
        print w3
    if(a.POST.get('warehouse4')):
        ticker4 = str(a.POST.get('warehouse4'))
        asset4 = aggressive(ticker4, start, end, name='asset4')
        t4 = bt.run(asset4)
        # merge4 = t4.data
        # data = bt.merge(merge4)
        w4 = float(a.POST.get('store4'))
        weights['asset4'] = w4
        print w4
    if(a.POST.get('warehouse5')):
        ticker5 = str(a.POST.get('warehouse5'))
        asset5 = aggressive(ticker5, start, end, name='asset5')
        t5 = bt.run(asset5)
        # merge1 = t5.data
        # data = bt.merge(merge5)
        w5 = float(a.POST.get('store5'))
        weights['asset5'] = w5
        print w5
    if(a.POST.get('warehouse6')):
        ticker6 = str(a.POST.get('warehouse6'))
        asset6 = aggressive(ticker6, start, end, name='asset6')
        t6 = bt.run(asset6)
        # merge6 = t6.data
        # data = bt.merge(merge6)
        w6 = float(a.POST.get('store5'))
        weights['asset6'] = w6
        print w6
    if(a.POST.get('warehouse7')):
        ticker7 = str(a.POST.get('warehouse7'))
        asset7 = aggressive(ticker7, start, end, name='asset7')
        t7 = bt.run(asset7)
        # merge7 = t1.data
        # data = bt.merge(merge7)
        w7 = float(a.POST.get('store7'))
        weights['asset7'] = w7
        print w7
    if(a.POST.get('warehouse8')):
        ticker8 = str(a.POST.get('warehouse8'))
        asset8 = aggressive(ticker8, start, end, name='asset8')
        t8 = bt.run(asset8)
        # merge8 = t8.data
        # data = bt.merge(merge8)
        w8 = float(a.POST.get('store8'))
        weights['asset8'] = w8
        print w8
    if(a.POST.get('warehouse9')):
        ticker9 = str(a.POST.get('warehouse9'))
        asset9 = aggressive(ticker9, start, end, name='asset9')
        
        t9 = bt.run(asset9)
        # merge9 = t9.data
        # data = bt.merge(merge9)
        w9 = float(a.POST.get('store9'))
        weights['asset9'] = w9
        print w9
    if(a.POST.get('warehouse10')):
        ticker10 = str(a.POST.get('warehouse10'))
        asset10 = aggressive(ticker10, start, end, name='asset10')
        t10 = bt.run(asset10)
        # merge10 = t10.data
        # data = bt.merge(merge10)
        w10 = float(a.POST.get('store10'))
        weights['asset10'] = w10
        print w10
    if(a.POST.get('warehouse11')):
        ticker11 = str(a.POST.get('warehouse11'))
        asset11 = aggressive(ticker11, start, end, name='asset11')
        t11 = bt.run(asset11)
        # merge11 = t11.data
        # data = bt.merge(merge11)
        w11 = float(a.POST.get('store11'))
        weights['asset11'] = w11
        print w11
    if(a.POST.get('warehouse12')):
        ticker12 = str(a.POST.get('warehouse12'))
        asset12 = aggressive(ticker12, start, end, name='asset12')
        t12 = bt.run(asset12)
        # merge12 = t12.data
        # data = bt.merge(merge12)
        w12 = float(a.POST.get('store12'))
        weights['asset5'] = w12
        print w12
        
    if(a.POST.get('warehouse13')):
        ticker13 = str(a.POST.get('warehouse13'))
        asset13 = aggressive(ticker13, start, end, name='asset13')
        t13 = bt.run(asset13)
        # merge13 = t13.data
        # data = bt.merge(merge13)
        w13 = float(a.POST.get('store13'))
        weights['asset13'] = w13
        print w13
    if(a.POST.get('warehouse14')):
        ticker14 = str(a.POST.get('warehouse14'))
        asset14 = aggressive(ticker14, start, end, name='asset14')
        t14 = bt.run(asset14)
        # merge14 = t14.data
        # data = bt.merge(merge14)
        w14 = float(a.POST.get('store14'))
        weights['asset14'] = w14
        print w14
    if(a.POST.get('warehouse15')):
        ticker15 = str(a.POST.get('warehouse15'))
        asset15 = aggressive(ticker14, start, end, name='asset15')
        t15 = bt.run(asset15)
        # merge15 = t15.data
        # data = bt.merge(merge15)
        w15 = float(a.POST.get('store15'))
        weights['asset15'] = w15
        print w15
    
    print weights  
    data = bt.merge(t1['asset1'].prices, t2['asset2'].prices)
    s = bt.Strategy('s', [bt.algos.SelectAll(), bt.algos.WeighSpecified(**weights),bt.algos.Rebalance()])
    print "uuuuu", s
    t = bt.Backtest(s, data)
    print "oooooo",t
    res = bt.run(t)
    
    res.plot()
    res.display()





def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            print user
            login(request, user)
            return redirect('dashboard:home')
    else:
        form = SignUpForm()
    return render(request, 'main/signup.html', {'form': form})



    #Valerian Aggressive


