openerp.library_module = function(instance, local) {
    var _t = instance.web._t,
        _lt = instance.web._lt;
    var QWeb = instance.web.qweb;

    local.HomePage = instance.Widget.extend({
        start: function() {
            template: "TestTemplate",
            this.$el.append(QWeb.render("TestTemplate"));
            
        },
    });
    
    local.Prova = instance.Widget.extend({
        start: function() {
            template: "TestFunction",
            this.$el.append(QWeb.render("TestFunction"));
            
        },
        
    });
    
    //local.Json = instance.Widget.extend({
    //    openerp.session.rpc('/my_url/some_json', 
    //        {}
    //    ).then(function (result) {
    //        return "ciao"
    //    }, function () {
    //        return "non ciao"
    //    });
    
  
    instance.web.client_actions.add('test.table', 'instances.library_module.HomePage');
    instance.web.client_actions.add('test.function', 'instances.library_module.Prova');
      
}


