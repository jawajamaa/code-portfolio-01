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
            .then(ImagesData => {
                setImages(ImagesData);
                
                const randomIdxFunc = () => {
                    if (ImagesData.length === 0) return;
                    const randomIdx = (Math.floor(Math.random() * ImagesData.length));
                    if ((ImagesData[randomIdx])?.horizontal === true){
                        setRandomImage(ImagesData[randomIdx]);
                    } else {
                        randomIdxFunc();
                    }
                };
                randomIdxFunc();
            });
    }, [baseUrl, imageUrl]);

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
