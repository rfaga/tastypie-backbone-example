var APP = APP || {};

APP.Operation = Backbone.Model.extend({
    base_url: function() {
      var temp_url = Backbone.Model.prototype.url.call(this);
      return (temp_url.charAt(temp_url.length - 1) == '/' ? temp_url : temp_url+'/');
    },
    url : '/api/operation/',
});

APP.Operations = Backbone.Collection.extend({
	model : APP.Operation,
	url : '/api/operation/',
});


APP.GridView = Backbone.View.extend({
	el : $("#grid_container"),
	events : {
		'click a.new-item': "newItem",
	},
	newItem : function(event){
		event.preventDefault();
		this.collection.create();
	},	
	render : function(){
		var self = this;
		this.collection = new APP.Operations();
		
		this.collection.fetch({reset: true});
    
		// Starting columns
		var columns = [{
			name : "id",
			label : "ID",
			editable : false,
			cell : 'string'
		}, {
			name : "description",
			label : "Descricao",
			cell : 'string'
		}, {
			name : "value",
			label : "Valor",
			cell : 'string'
		}, {
			name : "date",
			label : "Data",
			cell : 'date'
		}];

		var self = this;
		
		// Initialize a new Grid instance
		this.grid = new Backgrid.Grid({
		  columns: columns,
		  collection: this.collection
		});
		
		// listening edition
		this.grid.listenTo(this.collection,"backgrid:edited",function(e){
			e.url = e.base_url();
			e.save();
		});
		
		// add filtering
		var filter = new Backgrid.Extension.ClientSideFilter({
		  collection: self.collection,
		  fields: ['description']
		});
		
		// rendering elements
		this.$el.append(filter.render().$el);
		
		this.$el.append(this.grid.render().$el);
		
		
	}
});

var gridView = new APP.GridView();
gridView.render();

/*
var Route = Backbone.Router.extend({

	routes : {
		"index" : "index",
		//"edit/:model":        "edit",
		'*path' : 'index'
	},
	index : function() {
		gridView.render();
	}
}); 


var urls = new Route;

Backbone.history.start();
*/
