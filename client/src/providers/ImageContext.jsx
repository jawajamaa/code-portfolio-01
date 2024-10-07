import React, { createContext, useContext, useEffect, useState } from "react";

import { useUrl } from "./UrlContext";

const ImagesContext = createContext();

export function ImagesProvider({ children }) {
    const { baseUrl, imageUrl } = useUrl();
    const [images, setImages] = useState([]);
    const [randomImage, setRandomImage] = useState(null);


    useEffect(()=>{
        fetch(`${baseUrl + imageUrl}`)
            .then(r => r.json())
            .then(data => {
                setImages(data);
                const randomIdx = Math.floor(Math.random() * data.length);
                if ((data[randomIdx])?.horizontal === true){
                    setRandomImage(data[randomIdx]);
                }
            });
    }, []);

    console.log(randomImage?.horizontal);

    return(
        <ImagesContext.Provider value = {{ images, setImages, randomImage, setRandomImage }}>
            { children }
        </ImagesContext.Provider>
    );
}

export function useImages() {
    return useContext(ImagesContext);
}
