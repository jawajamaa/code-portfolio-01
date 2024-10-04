import React from "react";
import { Box, Container, Typography } from "@mui/material";

import { useImages } from "../providers/ImageContext";

function PhotographyMain(){
    const { images, setImages, randomImage, setRandomImage } = useImages(); 

    console.log(randomImage);
    console.log(images);

    return(
        <Box sx={{ flexGrow:1 }}>
            {randomImage && (
                <Container>
                    <img
                        src = { randomImage.path }
                        alt = { randomImage.title }
                        width = "750"
                    />
                </Container>
            )}
        </Box>
    )
};

export default PhotographyMain;
