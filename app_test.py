from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle

app.config["TESTING"] = True
app.config["DEBUG_TB_HOSTS"] = ["dont-show-debug-toolbar"]


class FlaskTests(TestCase):

    
    def test_route(self):
        #Test Home Page ("/")
        with app.test_client() as client:
            res = client.get("/")
            html=res.get_data(as_text=True)
            self.assertEqual(res.status_code,200)
            self.assertIn("<title>HomePAGE</title>",html)
            self.assertEqual(session["answer"],[])
            self.assertEqual(session["score"],0)
            self.assertIn('game', session)
    
    def test_game_route(self):
        with app.test_client() as client:
            res = client.get("/start")
            html=res.get_data(as_text=True)
            self.assertEqual(res.status_code,200)
            self.assertIn('<input type="text" id="guess" name="guess">',html)
    
