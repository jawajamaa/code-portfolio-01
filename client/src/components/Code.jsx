import { Box, Grid2, Typography } from "@mui/material";
import resume from "../../public/documents/Ryon-Timothy_Resume.pdf";

function Code() {
    return(
        <Box sx={{ flexGrow:1 }}>
            <Grid2 container spacing={2}>
                <Grid2 size={12}>
                    <Typography>01100011 01101111 01100100 01100101 </Typography>
                </Grid2>
                <Grid2 size={12}>
                    <a href={resume} download="Ryon-Timothy_Resume">Download my Resume</a>
                </Grid2>
            </Grid2>
        </Box>
    );
}

export default Code;
