// teste.js
// arquivo para teste de conexão ao MongoDB

//requer o módulo "mongoClient" 
var MongoClient = require('mongodb').MongoClient;

//configurações do nosso mongodb
var connectionUrl = 'mongodb://localhost:27017/meuprojeto',
    sampleCollection = 'capitulos';

//Precisamos inserir esses conteúdos em nosso mongoDB
var chapters = [{
    'Titulo': 'Teste de Node',
    'Autor': 'Vitor Mazuco'
},{
    'Titulo': 'Teste de Mongo',
    'Autor': 'Vitor Mazuco'
}];

MongoClient.connect(connectionUrl, function(err, db) {

  console.log("Conectado corretamente ao servidor");

  // Obter alguma coleção
  var collection = db.collection(sampleCollection);

  collection.insert(chapters,function(error,result){
    //aqui o resultado conterá uma matriz de registros inseridos
    if(!error) {
      console.log("Sucesso :"+result.ops.length+" capitulos inseridos!");
    } else {
      console.log("Algum erro foi encontrado!");
    }
    db.close();
  });
});
