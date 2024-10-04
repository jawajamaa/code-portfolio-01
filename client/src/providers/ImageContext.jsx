import React, { createContext, useContext, useEffect, useState } from "react";

import { useUrl } from "./UrlContext";

const ImagesContext = createContext();

export function ImagesProvider({ children }) {
    const { baseUrl, imageUrl } = useUrl();
    const [images, setImages] = useState([]);
    const [randomImage, setRandomImage] = useState(null);

    console.log(baseUrl);
    console.log(imageUrl);
    console.log(images);

    const randomIdx = () => {
        return Math.floor(Math.random() * data.length)
    }
    // function randomIdx() {
    //     return Math.floor(Math.random() * data.length)
    // }

    useEffect(()=>{
        fetch(`${baseUrl + imageUrl}`)
            .then(r => r.json())
            .then(data => {
                setImages(data);
                // const randomIdx = Math.floor(Math.random() * data.length);
                setRandomImage(data[randomIdx]);
                if (randomImage.horizontal && randomImage.horizontal !== true){
                    setRandomImage(data[randomIdx]);
                }
            });
    }, []);

    console.log(randomImage);

    return(
        <ImagesContext.Provider value = {{ images, setImages, randomImage, setRandomImage }}>
            { children }
        </ImagesContext.Provider>
    );
}

export function useImages() {
    return useContext(ImagesContext);
}
