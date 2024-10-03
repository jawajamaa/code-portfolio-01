import React from "react";
import { Typography } from "@mui/material";

import { useImages } from "../providers/ImageContext";

function PhotographyMain(){
    const { images, setImages, randomImage, setRandomImage } = useImages(); 

    console.log(randomImage);
    console.log(images);

    return(
        <Typography>
            Photography Main 1979
        </Typography>
    )
};

export default PhotographyMain;
