{
	'name' : 'Library',
	'version' : '1.0',
	'author' : 'Eriberto',
	'website' : 'http://www.eriberto.com',
	'category' : 'Tools',
	'depends' : ['base', 'board'],
	'description' : 'La tua libreria digitale!',
	'update_xml' : ['views/book_view.xml', 'views/author_view.xml', 'views/category_view.xml', 'views/buyer_view.xml', 'views/nationality_view.xml'],
	'data': [
        'security/ir.model.access.csv',
        'views/library_board.xml',
        'views/menu_view.xml',
        'views/templates.xml',
        'views/authors_list_controller.xml'
        
	],
	'installable': True
}
