let chevaux = [];

function ajouter() {

    const cheval = {
        numero: Number(document.getElementById("numero").value),
        nom: document.getElementById("nom").value,
        forme: Number(document.getElementById("forme").value),
        regularite: Number(document.getElementById("regularite").value),
        distance: Number(document.getElementById("distance").value),
        terrain: Number(document.getElementById("terrain").value),
        jockey: Number(document.getElementById("jockey").value),
        entraineur: Number(document.getElementById("entraineur").value),
        valeur: Number(document.getElementById("valeur").value),
        corde: Number(document.getElementById("corde").value),
        cote: Number(document.getElementById("cote").value)
    };

    chevaux.push(cheval);

    afficherTableau();

    document.querySelectorAll("input").forEach(input => input.value = "");
}

function afficherTableau() {

    const tbody = document.getElementById("liste");

    tbody.innerHTML = "";

    chevaux.forEach((c, index) => {

        tbody.innerHTML += `
        <tr>
            <td>${c.numero}</td>
            <td>${c.nom}</td>
            <td>${c.forme}</td>
            <td>${c.cote}</td>
            <td>
                <button onclick="supprimer(${index})">❌</button>
            </td>
        </tr>`;
    });

}

function supprimer(index){

    chevaux.splice(index,1);

    afficherTableau();

}

async function envoyer(){

    if(chevaux.length===0){

        alert("Ajoutez au moins un cheval.");

        return;

    }

    const reponse = await fetch("http://127.0.0.1:8000/analyse",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify(chevaux)

    });

    const resultat = await reponse.json();

    document.getElementById("resultat").textContent =
        JSON.stringify(resultat,null,2);

}
