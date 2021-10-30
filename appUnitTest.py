import unittest
import app


names = []
[names.append(i['name']) for i in app.documents]
names = set(names)


documents = [
    'passport "2207 876234" "Василий Гупкин"',
    'invoice "11-2" "Геннадий Покемонов"',
    'insurance "10006" "Аристарх Павлов"'
    ]


documents2 = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"}
    ]



class TestSomething(unittest.TestCase):
    def setUp(self):
        print("method setUp")


    def tearDown(self):
        print("method tearDown")


    def test_get_all_doc_owners_names(self):
        self.assertEqual(app.get_all_doc_owners_names(), names)


    def test_show_all_docs_info(self):
        self.assertEqual(app.show_all_docs_info(), documents)


    def test_doc_owner_name(self):
        self.assertEqual(app.get_doc_owner_name("11-2"), "Геннадий Покемонов")


    def test_get_doc_shelf(self):
        self.assertEqual(app.get_doc_shelf("10006"), "2")


    def test_add_new_doc(self):
        app.add_new_doc('номер', 'тип', 'имя', 'полка')
        self.assertIn({"type": "тип", "number": "номер", "name": "имя"}, app.documents)
        app.delete_doc("номер")


    def docs_for_test_delete_doc(self):
        doc = []
        for i in [i['number'] for i in app.documents]:
            doc.append(i)
        return doc


    def test_delete_doc(self):
        app.documents.append({"type": "pass", "number": "55555", "name": "Чехов"})
        self.assertNotIn(app.delete_doc("55555")[0], self.docs_for_test_delete_doc())


    def test_add_new_shelf(self):
        self.assertIn(app.add_new_shelf('10')[0], app.directories.keys())
        del app.directories['10']


if __name__ == '__main__':
    unittest.main()