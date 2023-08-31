import React, { useState } from "react";
const TextEditor = () => {
  const [text, setText] = useState("");
  const handleChange = (e) => {
    setText(e.target.value);
  };
  return (
    <div className="text-editor">
      <textarea value={text} onChange={handleChange} />
    </div>
  );
};
export default TextEditor;
