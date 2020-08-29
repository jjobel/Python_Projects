
'''
X-Ray Pixel Analyzing Tool XPAT - A tool used to compute statistical values for images within catalogue files using dmstat.

XPAT is an extension to the MATCha pipleline.
'''
from ciao_contrib.runtool import dmstat

num = int(input('Enter Catalog Number: '))
obs = int(input('Enter Obsid: '))


Stats = dmstat("/data1/devon/y3a2/current/observations/{}/I/flux_band1_thresh.expmap[sky=region(/data1/devon/y3a2/current/clusters/catalogue_{}/region_{}_r500_source.reg)]".format(obs, num, obs), centroid=False)

print(Stats)