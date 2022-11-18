from boggle import Boggle
from flask import Flask,request,render_template,redirect,flash,session,jsonify
from flask_debugtoolbar import DebugToolbarExtension

app=Flask(__name__)
app.config["SECRET_KEY"] = "test1234"
debug=DebugToolbarExtension(app)
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"]= False

boggle_game = Boggle()




@app.route("/")
def main():
    game = boggle_game.make_board()
    session["game"]= game
    session["answer"]=[]
    session["score"]=0
    session["message"]=""
    return render_template("base.html")

@app.route("/start",methods=["GET","POST"])
def start():
    
    if request.method == "POST":
        answer=request.get_json()['guess']
        answer_check = boggle_game.check_valid_word(session["game"],answer)
        answer_list = session["answer"]
        session["answer"] = answer_list
        if answer_check == "ok" and answer not in answer_list:
            session["score"] += len(answer)
            answer_list.append(answer)
            session["message"]= answer_check
        elif answer in answer_list:
            session["message"] = "Already USED"
        else:
            session["message"]=answer_check
        
        print(answer_list)
        print(session["score"])

        res = jsonify({"result":answer_check,
        "Score":session["score"],
        "display":session["message"]})
        return res
    
    
    return render_template("board.html")



