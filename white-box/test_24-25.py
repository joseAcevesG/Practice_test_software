import unittest

from whilte_box import DocumentEditingSystem, UserAuthentication


class TestUserAuthentication(unittest.TestCase):
    def setUp(self):
        self.user_auth = UserAuthentication()

    def test_initial_state(self):
        self.assertEqual(self.user_auth.state, "Logged Out")

    def test_login(self):
        self.assertEqual(self.user_auth.login(), "Login successful")
        self.assertEqual(self.user_auth.state, "Logged In")

    def test_invalid_login(self):
        self.user_auth.state = "Logged In"
        self.assertEqual(
            self.user_auth.login(), "Invalid operation in current state"
        )

    def test_logout(self):
        self.user_auth.state = "Logged In"
        self.assertEqual(self.user_auth.logout(), "Logout successful")
        self.assertEqual(self.user_auth.state, "Logged Out")

    def test_invalid_logout(self):
        self.assertEqual(
            self.user_auth.logout(), "Invalid operation in current state"
        )


class TestDocumentEditingSystem(unittest.TestCase):
    def setUp(self):
        self.doc_edit = DocumentEditingSystem()

    def test_initial_state(self):
        self.assertEqual(self.doc_edit.state, "Editing")

    def test_save_document(self):
        self.assertEqual(
            self.doc_edit.save_document(), "Document saved successfully"
        )
        self.assertEqual(self.doc_edit.state, "Saved")

    def test_invalid_save_document(self):
        self.doc_edit.state = "Saved"
        self.assertEqual(
            self.doc_edit.save_document(), "Invalid operation in current state"
        )

    def test_edit_document(self):
        self.doc_edit.state = "Saved"
        self.assertEqual(self.doc_edit.edit_document(), "Editing resumed")
        self.assertEqual(self.doc_edit.state, "Editing")

    def test_invalid_edit_document(self):
        self.assertEqual(
            self.doc_edit.edit_document(), "Invalid operation in current state"
        )


if __name__ == "__main__":
    unittest.main()
