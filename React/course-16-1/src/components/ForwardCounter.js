import Card from "./Card";
import useCounter from "../hook/use-counter";

const ForwardCounter = () => {
  const counter = useCounter();

  return <Card>{counter}</Card>;
};

export default ForwardCounter;
