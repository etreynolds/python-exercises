from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    def setUp(self):
        """Stuff to do before every test"""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        """Make sure everything starts up and display correctly"""

        with self.client:
            res = self.client.get('/')
            decoded = res.data.decode()
            self.assertIn("Score: 0", decoded)
            self.assertIn("Times Played: 0", decoded)
            self.assertIn("High Score: 0", decoded)
            self.assertIn("board", session)
            self.assertIsNone(session.get("highscore"))
            self.assertIsNone(session.get("numplays"))

    def test_valid_word(self):
        """Test if a word is valid compared to board put in session"""

        with self.client as client:
            with client.session_transaction() as sess:
                sess['board'] = [["R", "O", "K", "R", "T"],
                                 ["C", "C", "T", "T", "T"],
                                 ["C", "A", "T", "T", "T"],
                                 ["C", "A", "T", "T", "T"],
                                 ["C", "A", "T", "T", "T"]]
        response = self.client.get('/check-word?word=rock')
        self.assertEqual(response.json['response'], 'ok')
