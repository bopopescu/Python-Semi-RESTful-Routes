from system.core.router import routes


routes['default_controller'] = 'Products'
routes['GET']['/products/add_form'] = 'Products#add_form'
routes['POST']['/products/create'] = 'Products#create'
routes['GET']['/products/show/<id>'] = 'Products#show_page'
routes['POST']['/products/<id>'] = 'Products#destroy'
routes['GET']['/products/edit/<id>']='Products#edit_page'
routes['POST']['/products/update/<id>']='Products#update'
