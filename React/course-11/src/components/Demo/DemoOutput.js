import React from "react";

const DemoOutput = (props) => {
  console.log("DemoOutput RUNNUNG!!");
  return <p>{props.show ? "This is paragraph" : ""}</p>;
};

export default React.memo(DemoOutput);
