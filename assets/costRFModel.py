import statistics
from sklearn.metrics.scorer import make_scorer
import numpy as np
import pandas as pd


def getNoharm(data):
    std_harm = statistics.stdev(data['lnmorts_pph'])
    mean_harm = statistics.mean(data['lnmorts_pph'])
    harm_max = mean_harm + 3 * std_harm
    tempharm = pd.DataFrame(data['lnmorts_pph'])
    idx_max = tempharm[tempharm.gt(harm_max)].index[0]
    tempharm.loc[idx_max] = harm_max
    tempharmcent = (tempharm[:] / tempharm.max()[0]) * 100
    noharm = 100 - tempharmcent
    return noharm


def RFPPHLoss(truth, pred, data):
    noharm = getNoharm(data)
    tp = np.intersect1d(np.where(np.array(truth) == 1), np.where(np.array(pred) == 1))
    tn = np.intersect1d(np.where(np.array(truth) == 0), np.where(np.array(pred) == 0))
    fp = np.intersect1d(np.where(np.array(truth) == 0), np.where(np.array(pred) == 1))
    fn = np.intersect1d(np.where(np.array(truth) == 1), np.where(np.array(pred) == 0))

    ## true positive score = +1
    score1 = tp.shape[0]
    ebl1 = data['eblcat']
    ebl1 = ebl1[tp]
    eblscore1 = ((ebl1 == 2).sum()) * 1 + ((ebl1 == 3).sum()) * 2 + ((ebl1 == 4).sum()) * 4
    score1total = score1 + eblscore1

    ## true negative score = +3; reward noharm
    score2 = tn.shape[0] * 3
    noharmtemp2 = (((noharm.iloc[tn]).sum() / noharm.sum()[0]) * 100)
    ebl2 = data['eblcat']
    ebl2 = ebl2[tn]
    eblscore2 = ((ebl2 == 2).sum()) * 1 + ((ebl2 == 3).sum()) * 2 + ((ebl2 == 4).sum()) * 4
    score2total = score2 - eblscore2 + noharmtemp2

    ## false positive score = -3; penalty noharm
    score3 = fp.shape[0] * -3
    noharmtemp3 = (((noharm.iloc[fp]).sum() / noharm.sum()[0]) * 100)
    ebl3 = data['eblcat']
    ebl3 = ebl3[fp]
    eblscore3 = ((ebl3 == 2).sum()) * 1 + ((ebl3 == 3).sum()) * 2 + ((ebl3 == 4).sum()) * 4
    score3total = score3 + eblscore3 - noharmtemp3

    ## false negative score = -1
    score4 = fn.shape[0]
    ebl4 = data['eblcat']
    ebl4 = ebl4[fn]
    eblscore4 = ((ebl4 == 2).sum()) * 1 + ((ebl4 == 3).sum()) * 2 + ((ebl4 == 4).sum()) * 4
    score4total = -score4 - eblscore4

    RFPPHLoss = score1total + score2total + score3total + score4total
    return RFPPHLoss

costpenaltyscore = make_scorer(RFPPHLoss, greater_is_better=True)
