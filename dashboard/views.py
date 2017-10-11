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

def weather_all(a):
    print "hi"
    print datetime.now
    start= a.POST.get('start_date')
    start = datetime.strptime(str(start), '%Y-%m-%d')
    print start
    end = a.POST.get('end_date')
    end = datetime.strptime(str(end), '%Y-%m-%d')
    print end
    l = []
    weights = {}
    if(a.POST.get('warehouse1')):
        ticker1 = str(a.POST.get('warehouse1'))
        l.append(ticker1)
        w1 = a.POST.get('store1')
        weights['asset1'] = w1
    if(a.POST.get('warehouse2')):
        ticker2 = str(a.POST.get('warehouse2'))
        l.append(ticker2)
        w2 = a.POST.get('store2')
        weights['asset2'] = w2
    if(a.POST.get('warehouse3')):
        ticker3 = str(a.POST.get('warehouse3'))
        l.append(ticker3)
        w3 = a.POST.get('store3')
        weights['asset3'] = w3
    if(a.POST.get('warehouse4')):
        ticker4 = str(a.POST.get('warehouse4'))
        l.append(ticker4)
        w4 = a.POST.get('store4')
        weights['asset4'] = w4
    if(a.POST.get('warehouse5')):
        ticker5 = str(a.POST.get('warehouse5'))
        l.append(ticker5)
        w5 = a.POST.get('store5')
        weights['asset5'] = w5
    if(a.POST.get('warehouse6')):
        ticker6 = str(a.POST.get('warehouse6'))
        l.append(ticker6)
        w6 = a.POST.get('store6')
        weights['asset6'] = w6
    if(a.POST.get('warehouse7')):
        ticker7 = str(a.POST.get('warehouse7'))
        l.append(ticker7)
        w7 = a.POST.get('store7')
        weights['asset7'] = w7
    if(a.POST.get('warehouse8')):
        ticker8 = str(a.POST.get('warehouse8'))
        l.append(ticker8)
        w8 = a.POST.get('store8')
        weights['asset8'] = w8
    if(a.POST.get('warehouse9')):
        ticker9 = str(a.POST.get('warehouse9'))
        l.append(ticker9)
        w9 = a.POST.get('store9')
        weights['asset9'] = w9
    if(a.POST.get('warehouse10')):
        ticker10 = str(a.POST.get('warehouse10'))
        l.append(ticker10)
        w10 = a.POST.get('store10')
        weights['asset10'] = w10
    if(a.POST.get('warehouse11')):
        ticker11 = str(a.POST.get('warehouse11'))
        l.append(ticker11)
        w11 = a.POST.get('store11')
        weights['asset11'] = w11
    if(a.POST.get('warehouse12')):
        ticker12 = str(a.POST.get('warehouse12'))
        l.append(ticker12)
        w12 = (a.POST.get('store12'))
        weights['asset12'] = w12
    if(a.POST.get('warehouse13')):
        ticker13 = str(a.POST.get('warehouse13'))
        l.append(ticker13)
        w13 = a.POST.get('store13')
        weights['asset13'] = w13
    if(a.POST.get('warehouse14')):
        ticker14 = str(a.POST.get('warehouse14'))
        l.append(ticker14)
        w14 = a.POST.get('store14')
        weights['asset14'] = w14
    if(a.POST.get('warehouse15')):
        ticker15 = str(a.POST.get('warehouse15'))
        l.append(ticker15)
        w15 = a.POST.get('store15')
        weights['asset15'] = w15
    print l

    ticker = l
    data = bt.get(ticker, start=start, end=end)
    # print dir(data)
    print data.head()
    # plots = data.plot(subplots=True, figsize=(10, 4))
    # plt.show()
    data = data.asfreq(freq='M', method='pad')
    EntryAlgorithm = data.ewm(span=6).mean()
    ExitAlgorithm = data.ewm(span=12).mean()
    tw= EntryAlgorithm.copy()
    tw[EntryAlgorithm>ExitAlgorithm]= 1.0
    tw[EntryAlgorithm<=ExitAlgorithm]= 0.0
    print weights
    s = bt.Strategy('Perissos All-Weather', [bt.algos.RunMonthly(),
                       bt.algos.SelectAll(),
                       bt.algos.WeighTarget(tw),
                       bt.algos.Rebalance()])
    print "uuuuuuuu",s
    test = bt.Backtest(s, data)
    print "oooooo",test
    
    s2 = bt.Strategy('Bench', [bt.algos.SelectAll(),
                              bt.algos.WeighEqually(),
                              bt.algos.Rebalance()])
    
    
    test1 = bt.Backtest(s2, data)
    
    res1 = bt.run(test, test1)
    res1.plot(figsize = (10, 10))
    plt.show()
    res1.display()
    res1.display_monthly_returns('Perissos All-Weather')
    res1.display_monthly_returns('Bench')
    return True

def bench(ticker, start, end, weights):
    data = bt.get(ticker, start=start, end=end)
    print data.head()

    data = data.asfreq(freq='M', method='pad')
    # plots = data.plot(subplots=True, figsize=(10, 4))
    # plt.show()
    weights = weights
    print weights
    EntryAlgorithm = data.ewm(span=6).mean()
    ExitAlgorithm = data.ewm(span=12).mean()
  
   
    tw= EntryAlgorithm.copy()
    tw[EntryAlgorithm>ExitAlgorithm]= 1.0
    tw[EntryAlgorithm<=ExitAlgorithm]= 0.0

    s2 = bt.Strategy('Bench', [bt.algos.SelectAll(),
                              bt.algos.WeighEqually(),
                              bt.algos.Rebalance()])
    return bt.Backtest(s2, data)



def aggressive(ticker, start, end):
    data = bt.get(ticker, start=start, end=end)
    print data.head()

    data = data.asfreq(freq='M', method='pad')
    # plots = data.plot(subplots=True, figsize=(10, 4))
    # plt.show()
    EntryAlgorithm = data.ewm(span=6).mean()
    ExitAlgorithm = data.ewm(span=12).mean()
  
   
    tw= EntryAlgorithm.copy()
    tw[EntryAlgorithm>ExitAlgorithm]= 1.0
    tw[EntryAlgorithm<=ExitAlgorithm]= 0.0

    s = bt.Strategy('Perissos All-Weather', [bt.algos.RunMonthly(),
                       bt.algos.SelectAll(),
                       bt.algos.WeighTarget(tw),
                       bt.algos.Rebalance()])
    return bt.Backtest(s, data)

def weather_agg(a):
    start= a.POST.get('start_date')
    start = datetime.strptime(str(start), '%Y-%m-%d')
    print start
    end = a.POST.get('end_date')
    end = datetime.strptime(str(end), '%Y-%m-%d')
    print end
    l = []
    r = []
    weights = {}
    if(a.POST.get('warehouse1')):
        ticker1 = str(a.POST.get('warehouse1'))
        asset1 = aggressive(ticker1, start, end)
        # result1 = bt.run(asset1)
        # print dir(result1)
        # r.append({'asset1':result1})
        l.append(ticker1)
        w1 = float(a.POST.get('store1'))
        weights['asset1'] = w1
    if(a.POST.get('warehouse2')):
        ticker2 = str(a.POST.get('warehouse2'))
        asset2 = aggressive(ticker2, start, end)
        # result2 = bt.run(asset2)
        # r.append({'asset2':result2})
        l.append(ticker2)
        w2 = float(a.POST.get('store2'))
        weights['asset2'] = w2
    if(a.POST.get('warehouse3')):
        ticker3 = str(a.POST.get('warehouse3'))
        l.append(ticker3)
        w3 = a.POST.get('store3')
        weights['asset3'] = w3
    if(a.POST.get('warehouse4')):
        ticker4 = str(a.POST.get('warehouse4'))
        l.append(ticker4)
        w4 = a.POST.get('store4')
        weights['asset4'] = w4
    if(a.POST.get('warehouse5')):
        ticker5 = str(a.POST.get('warehouse5'))
        l.append(ticker5)
        w5 = a.POST.get('store5')
        weights['asset5'] = w5
    if(a.POST.get('warehouse6')):
        ticker6 = str(a.POST.get('warehouse6'))
        l.append(ticker6)
        w6 = a.POST.get('store6')
        weights['asset6'] = w6
    if(a.POST.get('warehouse7')):
        ticker7 = str(a.POST.get('warehouse7'))
        l.append(ticker7)
        w7 = a.POST.get('store7')
        weights['asset7'] = w7
    if(a.POST.get('warehouse8')):
        ticker8 = str(a.POST.get('warehouse8'))
        l.append(ticker8)
        w8 = a.POST.get('store8')
        weights['asset8'] = w8
    if(a.POST.get('warehouse9')):
        ticker9 = str(a.POST.get('warehouse9'))
        l.append(ticker9)
        w9 = a.POST.get('store9')
        weights['asset9'] = w9
    if(a.POST.get('warehouse10')):
        ticker10 = str(a.POST.get('warehouse10'))
        l.append(ticker10)
        w10 = a.POST.get('store10')
        weights['asset10'] = w10
    if(a.POST.get('warehouse11')):
        ticker11 = str(a.POST.get('warehouse11'))
        l.append(ticker11)
        w11 = a.POST.get('store11')
        weights['asset11'] = w11
    if(a.POST.get('warehouse12')):
        ticker12 = str(a.POST.get('warehouse12'))
        l.append(ticker12)
        w12 = a.POST.get('store12')
        weights['asset12'] = w12
    if(a.POST.get('warehouse13')):
        ticker13 = str(a.POST.get('warehouse13'))
        l.append(ticker13)
        w13 = a.POST.get('store13')
        weights['asset13'] = w13
    if(a.POST.get('warehouse14')):
        ticker14 = str(a.POST.get('warehouse14'))
        l.append(ticker14)
        w14 = a.POST.get('store14')
        weights['asset14'] = w14
    if(a.POST.get('warehouse15')):
        ticker15 = str(a.POST.get('warehouse15'))
        l.append(ticker15)
        w15 = a.POST.get('store15')
        weights['asset15'] = w15
    # print l

    ticker = l
    print weights
    t = aggressive(ticker, start, end)
    
    

    # data = bt.merge(result1.prices, result2.prices)
    # print data

    # Valerian_aggressive = bt.Strategy('Valerian Aggressive', [bt.algos.SelectAll(),
    #                                 bt.algos.WeighSpecified(**weights),
    #                                 bt.algos.Rebalance()])
    
    # t = bt.Backtest(Valerian_aggressive, data)
    print t

    t1 = bench(ticker, start, end, weights)

    print t1

    res = bt.run(t, t1)

    res.plot(figsize = (10, 10))
    plt.show()
    res.display()
    res.display_monthly_returns('Perissos All-Weather')
    res.display_monthly_returns('Bench')





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


