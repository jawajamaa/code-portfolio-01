import App from "./components/App";
import Home from "./components/Home";
import ErrorPage from "./components/ErrorPage";
import PhotographyMain from "./components/PhotographyMain";
import Spaces from "./components/Spaces";
import Places from "./components/Places";
import SpacesOverlay from "./components/SpacesOverlay";
import PlacesOverlay from "./components/PlacesOverlay";
import Airports from "./components/Airports";
import AirportsOverlay from "./components/AirportsOverlay";
import FromTheHip from "./components/FromTheHip";
import FromTheHipOverlay from "./components/FromTheHipOverlay";


const routes = [
    {
        path: "/",
        element: <App />,
        errorElement: <ErrorPage />,
        children: [
            {
                path: "/",
                element: <Home />
            },
            {
                path: "/photography",
                element: <PhotographyMain />,
            },
            {
                path: "/photography/spaces",
                element: <Spaces />
            },
            {
                path: "/photography/spaces/:id",
                element: <SpacesOverlay />
                // or just one Overlay component?Possibly not..
            },
            {
                path: "/photography/places",
                element: <Places />
            },
            {
                path: "/photography/places/:id",
                element: <PlacesOverlay />
            },
            {
                path: "/photography/airports",
                element: <Airports />
            },
            {
                path: "/photography/airports/:id",
                element: <AirportsOverlay />
            },
            {
                path: "/photography/from-the-hip",
                element: <FromTheHip />
            },
            {
                path: "/photography/from-the-hip/:id",
                element: <FromTheHipOverlay />
            },
        ]
    }
];

export default routes;
