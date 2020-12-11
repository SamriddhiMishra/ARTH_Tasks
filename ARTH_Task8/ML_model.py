import os

def color(n):
	os.system("tput setaf {}".format(n))
def model():
        color(3)
        print("\n\t ###### Linear Regression Model ######\n")
        color(6)
        os.system("pip3 install pandas")
        os.system("pip3 install sklearn")

        import pandas as pd


        df = pd.read_csv("hours_vs_scores.csv")
        print()
        color(2)
        print("########### Data imported successfully ###########")
        color(6)


        X_train = df.iloc[:,[0]].values
        y_train = df.iloc[:,1].values


        from sklearn.linear_model import LinearRegression
        reg = LinearRegression()
        reg.fit(X_train, y_train)
        print()
        color(2)
        print("########### Training complete ##############")
        color(6)
        print("Coefficient of the regression- " , reg.coef_[0])
        print("Y_Intercept of the regression- " , reg.intercept_)

        print("Y = "+str(reg.coef_[0])+"*X + "+str(reg.intercept_))
        #line = reg.coef_*X_train+reg.intercept_


        print()
        print("Please enter the No of Hours for which you want to predict the scores:- ")
        print("Kindly enter multiple values(if) in different lines -")
        print("Please press Enter then CTRL+D to stop entering:- ")
        os.system("cat > input.csv")
        df1 = pd.read_csv("input.csv", header=None)
        X_test = df1.iloc[:,[0]].values
        y_pred = reg.predict(X_test)

        y_pred = list(y_pred)
        color(2)
        print()
        print('''No of hours \t Predicted Scores
        ---------------------------------------''')

        for i in range(len(X_test)):
            print(int(X_test[i]),"\t\t",y_pred[i])
