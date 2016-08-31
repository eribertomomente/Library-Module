import openerp.http as http
from openerp.http import controllers_per_module

class TestController(http.Controller):

    @http.route('/cogito/<model("book.book"):book>/', auth='public', website=True)
    def book_info(self, book):
        #return http.request.render('book.author', {
        #'person': teacher
        return '<h1> Il libro intitolato  "' + str(book.title) + '"' + " e' stato scritto dall'autore " + '"' + str(book.author_id.nominative) + '"' + ' nato in "' + str(book.author_id.nationality_id.country)+ '" il giorno "' +str(book.author_id.born_date)+ '"</h1>'
        
    @http.route('/cogito/render_test', type='http')
    def view(self):
        return http.request.render('library_module.index_of_authors', { 
            'authors': ["Gabriele", "Giacomo", "Andrea"],
            'testo': "<strong>relazione del 09/08/2016</strong>"
        })

