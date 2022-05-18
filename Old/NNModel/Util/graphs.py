import seaborn
from sklearn import metrics
import matplotlib.pyplot as plt
from .helper import util_helper
import numpy as np
import pandas as pd
import os

"""

    Graphing Functions

"""

graph_fp = "/NNModel/GraphOutput/"

def parameter_tuning(v_loss, t_loss, title):
    plt.plot(v_loss, "o", 1, color="red", label="Validation loss")
    plt.plot(t_loss, "o", color="blue", label="Training loss")
    plt.title(title)
    plt.xlabel("Model")
    plt.ylabel("Loss")
    plt.legend(loc="upper right")
    # plt.show()
    cwd = makePath()
    plt.savefig(cwd + graph_fp + "parameterTuning.png")
    plt.close()

def learning_curve(learn_info): # for batch learning
    plt.plot(learn_info[0])
    plt.plot(learn_info[1])
    plt.title("accuracy over samples")
    plt.xlabel("Samples")
    plt.ylabel("Cost")
    plt.legend(["train", "loss"], loc="upper left")
    # plt.show()
    cwd = makePath()
    plt.savefig(cwd + graph_fp + "learningCurve.png")
    plt.close()

def confusion_matrix(prediction_info):
    y_pred = prediction_info[0]
    y_test = prediction_info[1]
    y_test_1d = util_helper(y_pred, y_test)
    y_pred_1d = util_helper(y_test, y_pred)
    cf_matrix = metrics.confusion_matrix(y_test_1d, y_pred_1d)
    ax = seaborn.heatmap(cf_matrix/np.sum(cf_matrix), annot=True, fmt=".2%", cmap="Reds")
    ax.set_title("Confusion Matrix\n")
    # ax.set_xlabel("\nPredicted Location")
    # ax.set_ylabel("Actual Location")
    # Ticket labels - List must be in alphabetical order
    # ax.xaxis.set_ticklabels(["""FILL IN"""])
    # ax.yaxis.set_ticklabels(["""FILL IN"""])
    # Display the visualization of the Confusion Matrix.
    # plt.show()
    cwd = makePath()
    plt.savefig(cwd + graph_fp + "confusionMatrix.png")
    plt.close()

def multi_roc_graph(prediction_info1, prediction_info2, extra=""):
    y_pred1 = prediction_info1[4]
    y_test1 = prediction_info1[1]
    y_pred2 = prediction_info2[4]
    y_test2 = prediction_info2[1]
    # results = util_helper(y_pred1, y_test1)
    fpr0, tpr0, thresholds0 = metrics.roc_curve(y_test1[:, 0], y_pred1[:, 0])
    auc0 = metrics.auc(fpr0, tpr0)
    plt.plot(fpr0, tpr0, color="maroon", lw=4, label="Model 1 ROC curve of class {0} (area = {1:0.2f})".format(0, auc0))    
    fpr1, tpr1, thresholds1 = metrics.roc_curve(y_test1[:, 1], y_pred1[:, 1])
    auc1 = metrics.auc(fpr1, tpr1)
    plt.plot(fpr1, tpr1, color="red", lw=3, label="Model 1 ROC curve of class {0} (area = {1:0.2f})".format(1, auc1))
    fpr0, tpr0, thresholds0 = metrics.roc_curve(y_test2[:, 0], y_pred2[:, 0])
    auc0 = metrics.auc(fpr0, tpr0)
    plt.plot(fpr0, tpr0, color="navy", lw=2, label="Model 2 ROC curve of class {0} (area = {1:0.2f})".format(0, auc0))    
    fpr1, tpr1, thresholds1 = metrics.roc_curve(y_test2[:, 1], y_pred2[:, 1])
    auc1 = metrics.auc(fpr1, tpr1)
    plt.plot(fpr1, tpr1, color="blue", lw=2, label="Model 2 ROC curve of class {0} (area = {1:0.2f})".format(1, auc1))
    plt.title("ROC Comparison Graph " + extra)
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.legend(loc="lower right")
    # plt.show()
    cwd = makePath()
    plt.savefig(cwd + graph_fp + "multiROC.png")
    plt.close()

def roc_graph(prediction_info, extra=""):
    y_pred = prediction_info[4]
    y_test = prediction_info[1]
    results = util_helper(y_pred, y_test)
    fpr0, tpr0, thresholds0 = metrics.roc_curve(y_test[:, 0], y_pred[:, 0])
    auc0 = metrics.auc(fpr0, tpr0)
    plt.plot(fpr0, tpr0, color="red", lw=4, label="ROC curve of class {0} (area = {1:0.2f})".format(0, auc0))    
    fpr1, tpr1, thresholds1 = metrics.roc_curve(y_test[:, 1], y_pred[:, 1])
    auc1 = metrics.auc(fpr1, tpr1)
    plt.plot(fpr1, tpr1, color="gold", lw=3, label="ROC curve of class {0} (area = {1:0.2f})".format(1, auc1))
    plt.title("ROC Graph " + extra)
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.legend(loc="lower right")
    # plt.show()
    cwd = makePath()
    plt.savefig(cwd + graph_fp + "ROC.png")
    plt.close()

def plotData(data):
    pdb_chart = pd.DataFrame(data, columns=['dist', 'omega', 'theta', 'phi'])
    seaborn.pairplot(pdb_chart)
    cwd = makePath()
    plt.savefig(cwd + graph_fp + "linearGraphing.png")
    
def makePath():
    cwd = os.getcwd()
    os.makedirs(os.path.dirname(cwd + graph_fp), exist_ok=True)
    return cwd