# -*- coding: utf-8 -*-
"""

Created on Sat Dec 24 07:31:47 2011

Author: Josef Perktold
"""

from __future__ import print_function
import numpy as np
import statsmodels.sandbox.stats.diagnostic as dia

canada_raw = '''\
     405.36646642737	    929.610513893698	    7.52999999999884	    386.136109062605
    404.639833965913	    929.803984550587	    7.69999999999709	    388.135759111711
    403.814883043744	    930.318387567177	    7.47000000000116	    390.540112911955
    404.215773188006	    931.427687420772	     7.2699999999968	    393.963817246136
    405.046713585284	    932.662005594273	    7.37000000000262	    396.764690917547
    404.416738673847	    933.550939726636	    7.12999999999738	    400.021701616327
     402.81912737043	    933.531526191785	    7.40000000000146	    400.751498688807
    401.977334663103	    933.076879439814	    8.33000000000175	    405.733473658807
    402.089724946428	     932.12375320915	    8.83000000000175	     409.05038628366
    401.306688373207	    930.635939140315	     10.429999999993	    411.398377747425
    401.630171263522	    929.097059933419	    12.1999999999971	    413.019421511595
     401.56375463175	    928.563335601161	    12.7700000000041	    415.166962884156
    402.815698906973	    929.069380060201	     12.429999999993	    414.662070678749
    403.142107624713	    930.265516098198	    12.2299999999959	    415.731936138368
    403.078619166324	    931.677031559203	    11.6999999999971	    416.231468866173
    403.718785733801	    932.138967575148	    11.1999999999971	     418.14392690728
    404.866799027579	    932.276686471608	    11.2700000000041	    419.735231229658
    405.636186735378	    932.832783118083	    11.4700000000012	    420.484186198549
    405.136285378794	    933.733419116009	    11.3000000000029	    420.930881402259
    406.024639922986	    934.177206176622	    11.1699999999983	    422.112404525291
    406.412269729241	    934.592839827856	                  11	    423.627805811063
    406.300932644569	    935.606709830033	    10.6300000000047	    423.988686751336
    406.335351723382	    936.511085968336	    10.2700000000041	    424.190212657915
    406.773695329549	    937.420090112655	    10.1999999999971	    426.127043353785
    405.152547649247	    938.415921627889	    9.66999999999825	    426.857794216679
    404.929830809648	    938.999170021426	    9.60000000000582	    426.745717993024
    404.576546350926	    939.235354789206	    9.60000000000582	    426.885793656802
    404.199492630983	    939.679504234357	                 9.5	    428.840253264144
     405.94985619596	    940.249674139969	                 9.5	    430.122322107039
     405.82209202516	    941.435818685214	    9.02999999999884	    430.230679154048
    406.446282537108	     942.29809597644	    8.69999999999709	    430.392994893689
    407.051247525876	    943.532223256403	    8.13000000000466	    432.028420083791
    407.946023990985	     944.34896981513	    7.87000000000262	    433.388625934544
    408.179584663105	    944.821488789039	    7.66999999999825	    433.964091817787
    408.599812740441	    945.067136927327	    7.80000000000291	    434.484384354647
    409.090560656008	     945.80672616174	     7.7300000000032	    436.156879277168
    408.704215141145	    946.869661504613	    7.56999999999971	    438.265143944308
    408.980275213206	    946.876612143542	    7.56999999999971	    438.763587343863
    408.328690037174	    947.249692256472	    7.33000000000175	    439.949811558539
    407.885696563307	    947.651276093962	    7.56999999999971	    441.835856392131
    407.260532233258	    948.183970741596	    7.62999999999738	    443.176872656863
    406.775150765526	    948.349239264364	    7.59999999999854	    444.359199033223
    406.179413590339	    948.032170661406	    8.16999999999825	    444.523614807208
    405.439793348166	    947.106483115935	    9.19999999999709	    446.969404642587
    403.279970790458	    946.079554231134	    10.1699999999983	    450.158586973168
    403.364855995771	    946.183811678692	    10.3300000000017	    451.546427290378
    403.380680430043	     946.22579516585	    10.3999999999942	    452.298351499968
    404.003182812546	    945.997783938785	    10.3699999999953	    453.120066578834
     404.47739841708	    945.518279080208	    10.6000000000058	    453.999145996277
    404.786782762866	    945.351397570438	                  11	    454.955176222477
    405.271003921828	    945.291785517556	    11.3999999999942	    455.482381155116
    405.382993140508	    945.400785900878	    11.7299999999959	    456.100929020225
    405.156416006566	    945.905809840959	     11.070000000007	    457.202696739531
    406.470043094757	     945.90347041344	    11.6699999999983	    457.388589594786
    406.229308967752	    946.319028746014	    11.4700000000012	    457.779898919191
    406.726483850871	    946.579621275764	    11.3000000000029	    457.553538085846
    408.578504884277	    946.780032223884	    10.9700000000012	     458.80240271533
     409.67671010704	    947.628284240641	    10.6300000000047	     459.05640335985
    410.385763295936	    948.622057553611	    10.1000000000058	     459.15782324686
    410.539523677181	    949.399183241404	    9.66999999999825	    459.703720275789
    410.445258303139	    949.948137966398	    9.52999999999884	    459.703720275789
    410.625605270832	    949.794494142446	    9.47000000000116	    460.025814162716
    410.867239714014	    949.953380175189	                 9.5	    461.025722503696
    411.235917829196	    950.250239444989	    9.27000000000407	     461.30391443673
    410.663655285725	    950.538030883093	                 9.5	      461.4030814421
    410.808508412624	    950.787128498243	    9.42999999999302	    462.927726133156
    412.115961520089	    950.869528648471	    9.69999999999709	    464.688777934061
    412.999407129539	    950.928132469716	    9.89999999999418	    465.071700094375
    412.955056755303	    951.845722481401	    9.42999999999302	    464.285125295526
     412.82413309368	      952.6004761952	    9.30000000000291	    464.034426099541
       413.048874899	    953.597552755418	    8.86999999999534	    463.453479461824
    413.611017876145	    954.143388344158	    8.77000000000407	    465.071700094375
    413.604781916778	    954.542593332134	    8.60000000000582	    466.088867474481
    412.968388225217	    955.263136106029	    8.33000000000175	    466.617120754625
    412.265886525002	    956.056052852469	    8.16999999999825	    465.747796561181
    412.910594097915	     956.79658640007	    8.02999999999884	    465.899527268299
    413.829416419695	    957.386480451857	    7.90000000000146	    466.409925351738
     414.22415210314	     958.06341570725	    7.87000000000262	    466.955244491812
      415.1677707968	    958.716592187518	    7.52999999999884	    467.628081344681
    415.701580225863	    959.488142422254	    6.93000000000029	     467.70256230891
    416.867407108435	    960.362493080892	    6.80000000000291	    469.134788222928
    417.610399060359	    960.783379042937	    6.69999999999709	    469.336419672322
    418.002980476361	    961.029029939624	    6.93000000000029	    470.011666329664
    417.266680178544	    961.765709811429	    6.87000000000262	    469.647234439539'''

canada = np.array(canada_raw.split(), float).reshape(-1,4)
k=2
resarch2 = dia.acorr_lm((canada[:,k]-canada[:,k].mean())**2, maxlag=2, autolag=None, store=1)
print(resarch2)
resarch5 = dia.acorr_lm(canada[:,k]**2, maxlag=12, autolag=None, store=1)

ss = '''\
        ARCH LM-test; Null hypothesis: no ARCH effects

Chi-squared = %(chi)-8.4f df = %(df)-4d p-value = %(pval)8.4g
'''
resarch = resarch5
print()
print(ss % dict(chi=resarch[2], df=resarch[-1].resols.df_model, pval=resarch[3]))


#R:FinTS: ArchTest(as.vector(Canada[,3]), lag=5)
'''
        ARCH LM-test; Null hypothesis: no ARCH effects

data:  as.vector(Canada[, 3])
Chi-squared = 78.878, df = 5, p-value = 1.443e-15
'''

#from ss above
'''
        ARCH LM-test; Null hypothesis: no ARCH effects

Chi-squared = 78.849   df = 5    p-value = 1.461e-15
'''

#k=2
#R
'''
        ARCH LM-test; Null hypothesis: no ARCH effects

data:  as.vector(Canada[, 4])
Chi-squared = 74.6028, df = 5, p-value = 1.121e-14
'''
#mine
'''
        ARCH LM-test; Null hypothesis: no ARCH effects

Chi-squared = 74.6028  df = 5    p-value = 1.126e-14
'''

'''
> ArchTest(as.vector(Canada[,4]), lag=12)

        ARCH LM-test; Null hypothesis: no ARCH effects

data:  as.vector(Canada[, 4])
Chi-squared = 69.6359, df = 12, p-value = 3.747e-10
'''

#mine:
'''
        ARCH LM-test; Null hypothesis: no ARCH effects

Chi-squared = 69.6359  df = 12   p-value = 3.747e-10
'''
