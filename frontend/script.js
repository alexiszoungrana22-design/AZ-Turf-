let chevaux=[];

function ajouter(){

chevaux.push({

numero:Number(numero.value),

nom:nom.value,

forme:Number(forme.value),

regularite:Number(regularite.value),

distance:Number(distance.value),

terrain:Number(terrain.value),

jockey:Number(jockey.value),

entraineur:Number(entraineur.value),

valeur:Number(valeur.value),

corde:Number(corde.value),

cote:Number(cote.value)

});

alert("Cheval ajouté");

}

async function envoyer(){

const r=await fetch("http://127.0.0.1:8000/analyse",{

method:"POST",

headers:{

"Content-Type":"application/json"

},

body:JSON.stringify(chevaux)

});

const data=await r.json();

resultat.textContent=JSON.stringify(data,null,2);

}
