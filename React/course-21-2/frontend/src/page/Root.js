import { Outlet, useNavigation } from "react-router-dom";
import MainNavgation from "../components/MainNavigation";

function RootLayout() {
  // const navigation = useNavigation();
  return (
    <>
      <MainNavgation />
      <main>
        {/* {navigation.state === "loading" && <p>Loading...</p>} */}
        <Outlet />
      </main>
    </>
  );
}

export default RootLayout;
