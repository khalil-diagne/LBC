import React, { useState } from 'react';

function Test(){
    const [compteur, setCompteur] = useState(0);
    function Decrement(){
        setCompteur(compteur - 1);
    }
    function Increment(){
        setCompteur(compteur + 1);
    }
    return (
        <div>
            <h1>Compteur : {compteur}</h1>
            <button onClick={() => Decrement()}>Decrement</button>
            <button onClick={() => Increment()}>Increment</button>  
        </div>
    );
}
export default Test;