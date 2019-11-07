import matplotlib.pyplot as plt
from random import randint
from collections import defaultdict
import itertools
##33
#
color_nucleo_marca = {'0':'#005A24','1':'#003214','2':'#7BB622','3':'#ED1C24','4':'#FCD511','5':'#0E8D89','6':'#8E9B9A','7':'#C9DBD9','8':'#545B5B','9':'#B2C1C0','10':'#008000','11':'#800000','12':'#00ff00','13':'#005f00','14':'#008700','15':'#00875f','16':'#00af00','17':'#00af5f','18':'#00af87','19':'#00afaf','20':'#00d700','21':'#00d75f','22':'#00d787','23':'#5f8700','24':'#5faf00','25':'#5faf5f','26':'#5fd700','27':'#5fd75f','28':'#5fd787','29':'#5fd7af','30':'#5fff00','31':'#5fff5f','32':'#5fff87','33':'#5fffaf','34':'#5fffd7','35':'#5fffff','36':'#87d700','37':'#87d75f','38':'#87d787','39':'#87d7af','40':'#87ff00','41':'#87ff5f','42':'#87ff87','43':'#87ffaf','44':'#87ffd7','45':'#87d7d7','46':'#87d7ff','47':'#87ffff','48':'#afd700','49':'#afd75f','50':'#afd787','51':'#afd7af','52':'#afd7d7','53':'#afd7ff','54':'#afff00','55':'#afff5f','56':'#afff87','57':'#afffaf','58':'#afffd7','59':'#afffff','60':'#ff0000','61':'#ff005f','62':'#d70000','63':'#d7005f','64':'#af0000','65':'#af005f','66':'#870000','67':'#87005f','68':'#5f0000','69':'#5f005f','70':'#800080','71':'#000080','72':'#0000ff','73':'#00005f','74':'#000087','75':'#0000af','76':'#0000d7','77':'#0000ff','78':'#005f87','79':'#005faf','80':'#005fd7','81':'#005fff','82':'#008787','83':'#0087af','84':'#0087d7','85':'#0087ff','86':'#00afd7','87':'#00afff','88':'#00d7d7','89':'#00d7ff','90':'#5f00ff','91':'#5f5fff','92':'#5f87d7','93':'#5f87ff','94':'#5fafd7','95':'#5fafff','96':'#ffaf00', '97':'#ff8700','98':'#ff5f00','99':'#d75f00','100':'#FFD700','101':'#ADFF2F','102':'#98FB98','103':'#90EE90','104':'#32CD32','105':'#3CB371', '106':'#2E8B57', '107':'#E0FFFF','108':'#AFEEEE','109':'#7FFFD4','110':'#40E0D0','111':'#48D1CC','112':'#00CED1','113':'#66CDAA','114':'#20B2AA','115':'#008B8B','116':"#333A5D",'117':'#61A139','118':'#4217E4','119':'#A7F3A4','120':'#3CFF3A','121':'#39877D','122':'#5EB2B6','123':'#73C8CB','124':'#85DB81','124':'#62341D','125':'#45661E','126':'#08A5E1','127':'#5BF77A','128':'#863326','129':'#8310F3','130':'#DAF5A3','131':'#73774E','132':'#A9C066','133':'#4AC89B','134':'#39BF8B','135':'#7BA595','136':'#65D59E','137':'#43D6BF','138':'#68F79D','139':'#12404C','140':'#BEA197','141':'#F7D348','142':'#98ECB5','143':'#552B8D','144':'#73E791','145':'#A5E964','146':'#2A56E0','147':'#35DF09','148':'#60D1A0','149':'#B5A6D7','150':'#115D95','151':'#3D2A0A','152':'#90B10F','153':'#76D9B8','154':'#570EA7','155':'#4A887A','156':'#55CC66','157':'#446600','158':'#014A29','159':'#F4F65C','160':'#85759F'}
color_nucleo_presentacion = {'0':'#005A24','1':'#003214','2':'#7BB622','3':'#ED1C24','4':'#FCD511','5':'#0E8D89','6':'#8E9B9A','7':'#C9DBD9','8':'#545B5B','9':'#B2C1C0','10':'#008000','11':'#800000','12':'#E39138','13':'#183B62','14':'#80E6BB','15':'#B1F3A4','16':'#50E78C','17':'#BC5A2D','18':'#7C79F9','19':'#B3D415','20':'#2B9EA4','21':'#F222EB','22':'#24BC48','23':'#E5B1AC','24':'#DD9327','25':'#445B32'}
listacolores=[]
for x in color_nucleo_marca:
	listacolores.append(color_nucleo_marca[x])
#
dictcolors = {i:listacolores[i] for i in range(0,len(listacolores))}


#for x in dictcolors:
#	print(dictcolors[x])
#print(dictcolors)
number_of_colors = len(listacolores)
#color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
#		for i in range(number_of_colors)]
#print(color[0])
#print(listacolores[0])
#
[(k, len(list(v))) for k, v in itertools.groupby(sorted(dictcolors.values()))]
#
#plt.subplot(2,2,2)
#for i in range(0,25):
#	plt.scatter(0, 10*i, c=dictcolors[i], s=100)
#3
#plt.subplot(2,2,1)
#for i in range(25,50):
#	plt.scatter(0,10*i, c=dictcolors[i], s=100)
#3
#plt.subplot(2,2,3)
#for i in range(50,80):
#	plt.scatter(0,10*i, c=dictcolors[i],s=100)

#plt.subplot(2,2,4)
#for i in range(80,110):
#	plt.scatter(0,10*i, c=dictcolors[i],s=100)

for i in range(number_of_colors):
	plt.scatter(i,i,c=dictcolors[i], s=20)
plt.show()
