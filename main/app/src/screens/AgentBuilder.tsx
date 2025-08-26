import React, { useState } from "react";
import { DndProvider, useDrag, useDrop } from "react-dnd";
import { HTML5Backend } from "react-dnd-html5-backend";

interface Tool {
  id: string;
  name: string;
}

// Dummy tool list
const tools: Tool[] = [
  { id: "1", name: "Text Analysis" },
  { id: "2", name: "Image Processing" },
  { id: "3", name: "Data Fetch" },
  { id: "4", name: "Code Execution" },
];

// Draggable Tool Item
const ToolItem: React.FC<{ tool: Tool }> = ({ tool }) => {
  const [{ isDragging }, drag] = useDrag(() => ({
    type: "TOOL",
    item: tool,
    collect: (monitor) => ({
      isDragging: !!monitor.isDragging(),
    }),
  }));

  return (
    <div
    //   ref={drag}
      className={`p-3 mb-2 rounded-lg cursor-move ${
        isDragging ? "bg-gray-700" : "bg-gray-800 hover:bg-gray-700"
      }`}
    >
      {tool.name}
    </div>
  );
};

// Drop Area
const DropArea: React.FC<{ onDrop: (tool: Tool) => void; selectedTools: Tool[] }> = ({
  onDrop,
  selectedTools,
}) => {
  const [, drop] = useDrop(() => ({
    accept: "TOOL",
    drop: (item: Tool) => onDrop(item),
  }));

  return (
    <div
    //   ref={drop}
      className="min-h-[300px] p-4 border-2 border-dashed border-gray-600 rounded-lg bg-gray-850 flex flex-col gap-2"
    >
      {selectedTools.length === 0 && (
        <p className="text-gray-400 text-center mt-10">Drag tools here to build your agent</p>
      )}
      {selectedTools.map((tool) => (
        <div key={tool.id} className="p-3 bg-gray-700 rounded-lg">
          {tool.name}
        </div>
      ))}
    </div>
  );
};

// Main Component
const AgentBuilder: React.FC = () => {
  const [selectedTools, setSelectedTools] = useState<Tool[]>([]);

  const handleDrop = (tool: Tool) => {
    if (!selectedTools.find((t) => t.id === tool.id)) {
      setSelectedTools((prev) => [...prev, tool]);
    }
  };

  return (
    <DndProvider backend={HTML5Backend}>
      <div className="p-8 min-h-screen flex flex-col md:flex-row gap-6">
        {/* Tool Selection */}
        <div className="md:w-1/3 p-4 bg-gray-800 rounded-lg">
          <h2 className="text-xl font-semibold mb-4">Available Tools</h2>
          {tools.map((tool) => (
            <ToolItem key={tool.id} tool={tool} />
          ))}
        </div>

        {/* Drop Area */}
        <div className="md:w-2/3 p-4 bg-gray-900 rounded-lg">
          <h2 className="text-xl font-semibold mb-4">Agent Builder</h2>
          <DropArea onDrop={handleDrop} selectedTools={selectedTools} />
        </div>
      </div>
    </DndProvider>
  );
};

export default AgentBuilder;
