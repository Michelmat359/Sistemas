import mlflow
import mlflow.xgboost
import xgboost as xgb
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def main():
    mlflow.set_tracking_uri("http://mlflow:5000")
    mlflow.xgboost.autolog()

    data = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)

    dtrain = xgb.DMatrix(X_train, label=y_train)
    dtest = xgb.DMatrix(X_test, label=y_test)

    params = {
        'objective': 'multi:softprob',
        'max_depth': 6,
        'num_class': 3,
        'eta': 0.1
    }
    num_round = 100

    model = xgb.train(params, dtrain, num_round)
    preds = model.predict(dtest)
    best_preds = preds.argmax(axis=1)
    acc = accuracy_score(y_test, best_preds)
    mlflow.log_metric('accuracy', acc)


if __name__ == "__main__":
    main()
