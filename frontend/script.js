let chevaux = [];

function ajouterCheval() {

    const numero = Number(document.getElementById("numero").value);
    const nom = document.getElementById("nom").value;
    const cote = Number(document.getElementById("cote").value);

    if (!numero || !nom || !cote) {
        alert("Veuillez remplir tous les champs.");
        return;
    }

    chevaux.push({
        numero: numero,
        nom: nom,
        cote: cote
    });

    afficherListe();

    document.getElementById("numero").value = "";
    document.getElementById("nom").value = "";
    document.getElementById("cote").value = "";
}

function afficherListe() {

    const liste = document.getElementById("listeChevaux");

    liste.innerHTML = "";

    chevaux.forEach((cheval) => {

        const li = document.createElement("li");

        li.textContent =
            `${cheval.numero} - ${cheval.nom} (Cote : ${cheval.cote})`;

        liste.appendChild(li);

    });

}

async function analyser() {

    if (chevaux.length === 0) {
        alert("Ajoutez au moins un cheval.");
        return;
    }

    try {

        const response = await fetch("/analyse", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(chevaux)

        });

        const resultat = await response.json();

        document.getElementById("resultat").textContent =
            JSON.stringify(resultat, null, 2);

    } catch (e) {

        document.getElementById("resultat").textContent =
            "Erreur de connexion avec le backend.";

    }

}
