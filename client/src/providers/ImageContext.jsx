import { createContext, useContext, useEffect, useState } from "react";

const ImagesContext = createContext();

export function ImagesProvider({ children }) {
    const [images, setImages] = useState([]);
    const [randomImage, setRandomImage] = useState(null);

    useEffect(()=>{
        fetch()
    })
}
