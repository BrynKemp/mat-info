import numpy as np
import pyreadr
import pandas as pd
import math
import pyreadr
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.calibration import CalibratedClassifierCV
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import brier_score_loss
import matplotlib.pyplot as plt
from sklearn.preprocessing import RobustScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import RepeatedStratifiedKFold
from numpy import mean
from numpy import sqrt
from numpy import argmax
from sklearn.metrics import roc_curve
from matplotlib import pyplot
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import auc
import statistics
from sklearn.metrics.scorer import make_scorer
import numpy as np
import pandas as pd


##############################################  Setup models  ##############################################

def to_labels(pos_probs, threshold):
    return (pos_probs <= threshold).astype('int')


def getppv(pred, test_y, harm1test, harm2test, sumharm1, sumharm2):
    test_no = np.where(pred == 0)
    test_yes = np.where(pred == 1)
    truth_no = np.where(testy == 0)
    truth_yes = np.where(testy == 1)

    tpset = np.intersect1d(truth_yes, test_yes)
    fpset = np.intersect1d(truth_no, test_yes)
    tnset = np.intersect1d(truth_no, test_no)
    fnset = np.intersect1d(truth_yes, test_no)

    tp_val = tpset.shape[0]
    fp_val = fpset.shape[0]
    tn_val = tnset.shape[0]
    fn_val = fnset.shape[0]

    sens = 0
    sens_num = tp_val
    sens_dom = tp_val + fn_val
    if sens_num != 0 and sens_dom != 0:
        sens = sens_num / sens_dom

    spec = 0
    spec_num = tn_val
    spec_dom = tn_val + tp_val
    if spec_num != 0 and spec_dom != 0:
        spec = spec_num / spec_dom

    ppv = 0
    ppv_num = tp_val
    ppv_dom = tp_val + fp_val
    if ppv_num != 0 and ppv_dom != 0:
        ppv = ppv_num / ppv_dom

    npv = 0
    npv_num = tn_val
    npv_dom = tn_val + fn_val
    if npv_num != 0 and npv_dom != 0:
        npv = npv_num / npv_dom

    frac_harm1 = 0
    if sum(harm1test) != 0:
        frac_harm1 = (sum(harm1test) / sumharm1) * 100

    frac_harm2 = 0
    if sum(harm2test) != 0:
        frac_harm2 = (sum(harm2test) / sumharm2) * 100

    listreturn = [sens, spec, ppv, npv, frac_harm1, frac_harm2]
    return listreturn


def getscores(X, pred_y, test_y, harm1test, harm2test, j, predtag, eblcattest):
    pred_y = pd.DataFrame(pred_y)
    harm1test = pd.DataFrame(harm1test)
    harm2test = pd.DataFrame(harm2test)
    test_y = pd.DataFrame(test_y)
    # td = [pred, harm1test, harm2test, truthtest]
    # td = pd.concat(td, axis=1)
    # td.columns = ['pred', 'harm1', 'harm2','truthtest']
    # td.sort_values(by='harm1', ascending=True)

    sumharm1 = sum(harm1test)
    sumharm2 = sum(harm2test)

    thresh_cent = np.arange(0.01, 1, 0.01)
    cent = 100 - np.arange(1, 100, 1)

    dummyarray = np.empty((100, 22))
    dummyarray[:] = np.nan
    output = pd.DataFrame(dummyarray)

    for a in range(0, 99, 1):

        test_thresh = thresh_cent[a]
        test_cent = cent[a]
        pharm_cent = np.percentile((harm2[harm2 > 0]), test_cent)
        # ppred_cent = np.percentile((td.harm2[td.pred2>0]), test_cent)

        # rows_h1cent = harm1test.index.values[harm1test >= pharm_cent]
        # rows_h2cent = harm2test.index.values[harm2test >= pharm_cent]
        # rows_pcent = td['pred'].index.values[td['pred'] >= pharm_cent]

        pred3 = to_labels(pred_y, test_thresh)
        # tempdata_h = td.iloc[rows_hcent, :]
        # temph_return = getppv(pred3, test_y, harm1test,harm2test, sumharm1, sumharm2)

        p3truth_yes = np.where(np.array(test_y) == 1)
        p3truth_no = np.where(np.array(test_y) == 0)
        p3screen_yes = np.where(np.array(pred3) == 1)
        p3screen_no = np.where(np.array(pred3) == 0)

        eblcat1 = np.where(np.array(eblcattest) == 1)
        eblcat2 = np.where(np.array(eblcattest) == 2)
        eblcat3 = np.where(np.array(eblcattest) == 3)
        eblcat4 = np.where(np.array(eblcattest) == 4)

        tp_temp_yes = np.where(p3screen_yes)
        tp_capture_pos = np.intersect1d(p3truth_yes, p3screen_yes)
        tp_capture_neg = np.intersect1d(p3truth_no, p3screen_no)

        harm2capture_tpos = 0
        if (harm2test[pred3 == 1].sum() > 0).bool():
            harm2capture_tpos = harm2test[pred3 == 1].sum() / harm2test.sum()

        harm2capture_pos = 0
        if (harm2test.iloc[tp_capture_pos].sum() > 0).bool():
            harm2capture_pos = harm2test.iloc[tp_capture_pos].sum() / harm2test.sum()

        harm2capture_tneg = 0
        if (harm2test[pred3 == 0].sum() > 0).bool():
            harm2capture_tneg = harm2test[pred3 == 0].sum() / harm1test.sum()

        harm2capture_neg = 0
        if (harm2test.iloc[tp_capture_neg].sum() > 0).bool():
            harm2capture_neg = harm2test.iloc[tp_capture_neg].sum() / harm2test.sum()

        ptn, pfp, pfn, ptp = confusion_matrix(test_y, pred3).ravel()

        # eblcat
        tp_eblcat1 = (np.intersect1d((np.intersect1d(p3truth_yes, p3screen_yes)), eblcat1)).shape[0]
        fp_eblcat1 = (np.intersect1d((np.intersect1d(p3truth_no, p3screen_yes)), eblcat1)).shape[0]
        tn_eblcat1 = (np.intersect1d((np.intersect1d(p3truth_no, p3screen_no)), eblcat1)).shape[0]
        fn_eblcat1 = (np.intersect1d((np.intersect1d(p3truth_yes, p3screen_no)), eblcat1)).shape[0]
        # eblcat2
        tp_eblcat2 = (np.intersect1d((np.intersect1d(p3truth_yes, p3screen_yes)), eblcat2)).shape[0]
        fp_eblcat2 = (np.intersect1d((np.intersect1d(p3truth_no, p3screen_yes)), eblcat2)).shape[0]
        tn_eblcat2 = (np.intersect1d((np.intersect1d(p3truth_no, p3screen_no)), eblcat2)).shape[0]
        fn_eblcat2 = (np.intersect1d((np.intersect1d(p3truth_yes, p3screen_no)), eblcat2)).shape[0]
        # eblcat 3
        tp_eblcat3 = (np.intersect1d((np.intersect1d(p3truth_yes, p3screen_yes)), eblcat3)).shape[0]
        fp_eblcat3 = (np.intersect1d((np.intersect1d(p3truth_no, p3screen_yes)), eblcat3)).shape[0]
        tn_eblcat3 = (np.intersect1d((np.intersect1d(p3truth_no, p3screen_no)), eblcat3)).shape[0]
        fn_eblcat3 = (np.intersect1d((np.intersect1d(p3truth_yes, p3screen_no)), eblcat3)).shape[0]
        # eblcat 4
        tp_eblcat4 = (np.intersect1d((np.intersect1d(p3truth_yes, p3screen_yes)), eblcat4)).shape[0]
        fp_eblcat4 = (np.intersect1d((np.intersect1d(p3truth_no, p3screen_yes)), eblcat4)).shape[0]
        tn_eblcat4 = (np.intersect1d((np.intersect1d(p3truth_no, p3screen_no)), eblcat4)).shape[0]
        fn_eblcat4 = (np.intersect1d((np.intersect1d(p3truth_yes, p3screen_no)), eblcat4)).shape[0]

        pspec = 0
        if ptn != 0:
            pspec = ptn / (ptn + pfp)

        psens = 0
        if ptp != 0:
            psens = ptp / (ptp + pfn)

        pppv = 0
        if ptp != 0:
            pppv = ptp / (ptp + pfp)

        pnpv = 0
        if ptn != 0:
            pnpv = ptn / (ptn + pfn)

        oapr = 0
        if ptp != 0 and pfp != 0:
            oapr = pfp / ptp

        oanr = 0
        if ptp != 0 and pfp != 0:
            oanr = pfn / ptn

        # ppv by eblcat
        pppv1 = 0
        if tp_eblcat1 != 0:
            pppv1 = tp_eblcat1 / (tp_eblcat1 + fp_eblcat1)

        pppv2 = 0
        if tp_eblcat2 != 0:
            pppv2 = tp_eblcat2 / (tp_eblcat2 + fp_eblcat2)

        pppv3 = 0
        if tp_eblcat3 != 0:
            pppv3 = tp_eblcat3 / (tp_eblcat3 + fp_eblcat3)

        pppv4 = 0
        if tp_eblcat4 != 0:
            pppv4 = tp_eblcat4 / (tp_eblcat4 + fp_eblcat4)

        # npv by eblcat
        pnpv1 = 0
        if tn_eblcat1 != 0:
            pnpv1 = tn_eblcat1 / (tn_eblcat1 + fn_eblcat1)

        pnpv2 = 0
        if tn_eblcat2 != 0:
            pnpv2 = tn_eblcat2 / (tn_eblcat2 + fn_eblcat2)

        pnpv3 = 0
        if tn_eblcat3 != 0:
            pnpv3 = tn_eblcat3 / (tn_eblcat3 + fn_eblcat3)

        pnpv4 = 0
        if tn_eblcat4 != 0:
            pnpv4 = tn_eblcat4 / (tn_eblcat4 + fn_eblcat4)

        fpr, tpr, _ = roc_curve(test_y, pred3)
        auc_score = auc(tpr, fpr)

        precision, recall, _ = precision_recall_curve(test_y, pred3)
        prc_score = auc(recall, precision)

        try:
            tempbrier = brier_score_loss(test_y, pred_y)
        except:
            tempbrier = 0

        try:
            t1 = harm2capture_tpos[0]
        except:
            t1 = 0
        try:
            t2 = harm2capture_pos[0]
        except:
            t2 = 1
        try:
            t3 = 1 - harm2capture_tneg[0]
        except:
            t3 = 1
        try:
            t4 = 1 - harm2capture_neg[0]
        except:
            t4 = 0

        output.iloc[a, 0] = test_thresh
        output.iloc[a, 1] = psens
        output.iloc[a, 2] = pspec
        output.iloc[a, 3] = pppv
        output.iloc[a, 4] = pnpv
        output.iloc[a, 5] = t1
        output.iloc[a, 6] = t2
        output.iloc[a, 7] = t3
        output.iloc[a, 8] = t4
        output.iloc[a, 9] = pppv1
        output.iloc[a, 10] = pppv2
        output.iloc[a, 11] = pppv3
        output.iloc[a, 12] = pppv4
        output.iloc[a, 13] = pnpv1
        output.iloc[a, 14] = pnpv2
        output.iloc[a, 15] = pnpv3
        output.iloc[a, 16] = pnpv4
        output.iloc[a, 17] = prc_score
        output.iloc[a, 18] = auc_score
        output.iloc[a, 19] = tempbrier
        output.iloc[a, 20] = oapr
        output.iloc[a, 21] = oanr

    output.columns = ['Thresh', 'pSens', 'pSpec', 'pPPV', 'pNPV', 'harmCaptureAllPos', 'harmCaptureTruePos',
                      'harmCaptureAllNeg', 'harm2CaptureTrueNeg', 'PPV_eblcat1', 'PPV_eblcat2', 'PPV_eblcat3',
                      'PPV_eblcat4', 'NPV_eblcat1', 'NPV_eblcat2', 'NPV_eblcat3', 'NPV_eblcat4', 'PRC', 'AUC', 'Brier',
                      'OAPR', 'OANR']

    if predtag == 'Yes':
        filename = 'Z:/2019/PPH/AnalysisMaster/ML/Data/Chromosomes/chr4list.xlsx'

    if predtag == 'No':
        filename = 'Z:/2019/PPH/AnalysisMaster/ML/Data/Chromosomes/chr4list.xlsx'
    output.to_excel(filename)

    return output


# results_df = results_df.append(new_row, ignore_index=True)

def calibrated2(X, y):
    RFModel = RandomForestClassifier(max_features='auto', max_samples=0.4, n_estimators=1250, max_depth=8,
                                     class_weight={0: 1, 1: 1.5})
    cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
    rfscores1 = cross_val_score(RFModel, X, y, scoring=costpenaltyscore, cv=cv, n_jobs=-1)
    rfscores2 = cross_val_score(RFModel, X, y, scoring='roc_auc', cv=cv, n_jobs=-1)
    rfscore1 = mean(rfscores1)
    rfscore2 = mean(rfscores2)
    #y_pred1 = cross_val_predict(RFModel, X, y, cv=cv, n_jobs=-1)
    y_pred2 = cross_val_predict(RFModel, X, y, cv=10, method='predict_proba')
    return y_pred2, rfscore1, rfscore2


def calibrated(trainX, testX, trainy):
    # define model
    rfmodel = RandomForestClassifier(max_features=5, max_samples=0.4, n_estimators=1250, max_depth=8,
                                     class_weight={0: 1, 1: 1.5})
    # define and fit calibration model
    calmod = CalibratedClassifierCV(rfmodel, method='sigmoid', cv=8)
    calmod.fit(trainX, trainy)

    # predict probabilities
    return calmod.predict_proba(testX)


def makechromosome(j, chromloci):
    chrom = chromloci.iloc[j, :]
    delchr = []
    for i in range(0, 29, 1):
        t = chrom.iloc[i]
        if not isinstance(t, str):
            if math.isnan(t):
                delchr.append(i)
    chromname = ("chrom%s" % j)
    chrom2 = np.delete(np.array(chrom), delchr)
    return chrom2


##############################################  Load Data  ##############################################

temp1 = pyreadr.read_r('Z:/2019/PPH/AnalysisMaster/ML/Data/datamodel.Rdata')
global data
data = temp1['tempmorb']

int_a = ['parity', 'age', 'ancount', 'gad', 'parity_2', 'age_2', 'ancount_2', 'gad_2', 'age_3', 'ancount_3', 'gad_3']
cats_a = ['eblcat']

for i in range(len(int_a)):
    name1 = int_a[i]
    data[name1] = data[name1].astype('int')

for i in range(len(cats_a)):
    name1 = cats_a[i]
    data[name1] = data[name1].astype('category')

temp2 = pyreadr.read_r('Z:/2019/PPH/AnalysisMaster/ML/Data/chromtemplate.Rdata')
chromloci = temp2['chromloci2']

global harm1
harm1 = data['morts_nopph'].copy()
harm1 = pd.DataFrame(harm1)

global harm2
harm2 = data['morts_pph'].copy()
harm2 = pd.DataFrame(harm2)

modset = data.iloc[:, 0:48]
eblcat = data['eblcat']

truth = data['truth'].astype('category')
truth = truth.cat.codes
features = np.array(list(data))
y = truth


############################################## Evaluate  ##############################################


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
    eblscore1 = ((ebl1 == 2).sum()) + ((ebl1 == 3).sum()) + ((ebl1 == 4).sum()) * 4
    score1total = score1 - eblscore1

    ## true negative score = +3; reward noharm
    score2 = tn.shape[0] * 3
    noharmtemp2 = (((noharm.iloc[tn]).sum() / noharm.sum()[0]) * 200)
    ebl2 = data['eblcat']
    ebl2 = ebl2[tn]
    eblscore2 = ((ebl2 == 2).sum()) + ((ebl2 == 3).sum()) + ((ebl2 == 4).sum()) * 4
    score2total = score2 - eblscore2 + noharmtemp2

    ## false positive score = -3; penalty noharm
    score3 = fp.shape[0] * -3
    noharmtemp3 = (((noharm.iloc[fp]).sum() / noharm.sum()[0]) * 200)
    ebl3 = data['eblcat']
    ebl3 = ebl3[fp]
    eblscore3 = ((ebl3 == 2).sum()) + ((ebl3 == 3).sum()) + ((ebl3 == 4).sum()) * 4
    score3total = score3 + eblscore3 - noharmtemp3

    ## false negative score = -1
    score4 = fn.shape[0]
    ebl4 = data['eblcat']
    ebl4 = ebl4[fn]
    eblscore4 = ((ebl4 == 2).sum()) + ((ebl4 == 3).sum()) + ((ebl4 == 4).sum()) * 4
    score4total = -score4 - eblscore4

    RFPPHLoss = score1total + score2total + score3total + score4total
    return RFPPHLoss


costpenaltyscore = make_scorer(RFPPHLoss, data=data, greater_is_better=True)

##############################################  Build DataSet  ##############################################

scores1 = []
scores2 = []

for a in range(chromloci.shape[0]):
    tchrom = makechromosome(a, chromloci)
    X = data[tchrom]
    pred, rfscore1, rfscore2 = calibrated2(X, y)
    scores1.append(rfscore1)
    scores2.append(rfscore2)
    exec(f'pred{a}=pred')


modelset = [pd.DataFrame(X), pd.DataFrame(harm1), pd.DataFrame(harm2), pd.DataFrame(eblcat)]
modseth = pd.concat(modelset, axis=1)
modseth = np.array(modseth)

trainX_m, testX_m, trainy, testy = train_test_split(modseth, y, test_size=0.33, random_state=2)
eblcattest = testX_m[:, testX_m.shape[1] - 1]
harm1test = testX_m[:, testX_m.shape[1] - 3]
harm2test = testX_m[:, testX_m.shape[1] - 2]
testX = testX_m[:, 0:testX_m.shape[1] - 4]
trainX = trainX_m[:, 0:trainX_m.shape[1] - 4]

preds = calibrated(trainX, testX, trainy)

pred_y = preds[:, 1]
pred_n = preds[:, 0]
testy_y = testy
testy_n = testy
testy_n = testy_n - 1
testy_n = abs(testy_n)

# predtag = 'Yes'
# output = getscores(X, pred_y, testy_y, harm1test, harm2test, 3, predtag, eblcattest)
