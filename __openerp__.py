{
	'name' : 'Book',
	'version' : '1.0',
	'author' : 'Eriberto',
	'website' : 'http://www.eriberto.com',
	'category' : 'Tools',
	'depends' : ['base'],
	'description' : 'La tua libreria digitale!',
	'update_xml' : ['book_view.xml', 'author_view.xml', 'category_view.xml', 'buyer_view.xml'],
	'data': [
        'security/ir.model.access.csv'
	],
	'installable': True
}
