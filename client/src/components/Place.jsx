import React from "react";
import { Box, ImageList, Typography } from "@mui/material";

import ImgCard from "./ImgCard";
import { useImages } from "../providers/ImageContext";


function Place(){
    const { images } = useImages();

    return(
        <Box sx={{ ml:-15, width: 1500, height: 750}}>
            <ImageList variant="masonry" cols={4} gap={8}>
                {
                    images?.map(img =>(
                        img.gallery === "Place" ?
                            <ImgCard
                                key = { img.id }
                                id = { img.id }
                                title = { img.title }
                                location = { img.location }
                                year = { img.year }
                                path = { img.path }
                            /> : null
                    ))
                }
            </ImageList>
        </Box>
    )
}

export default Place;
