import { useState, useEffect } from "react";

import Card from "./Card";
import useCounter from "../hook/use-counter";

const BackwardCounter = () => {
  const counter = useCounter(false);

  return <Card>{counter}</Card>;
};

export default BackwardCounter;
