import { Paper, styled } from "@mui/material";

const Item = styled(Paper)(({ theme }) => ({
    backgroundColor: "#6a716a",
    ...theme.typography.body2,
    padding: theme.spacing(1),
    textAlign: "center",
    color: theme.palette.text.secondary,
    ...theme.applyStyles("dark", {
        backgroundColor: "dark",
    }),
}));

export default Item;
