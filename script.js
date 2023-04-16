const nodes = document.querySelectorAll(".node");
const graph = document.querySelector(".graph");
let edge;

nodes.forEach(node => {
  node.addEventListener("mousedown", function(event) {
    event.preventDefault();
    const startX = event.clientX - graph.offsetLeft;
    const startY = event.clientY - graph.offsetTop;
    
    edge = document.createElement("div");
    edge.classList.add("edge");
    graph.appendChild(edge);
    
    document.addEventListener("mousemove", drawEdge);
    document.addEventListener("mouseup", finishEdge);
    
    function drawEdge(event) {
      const endX = event.clientX - graph.offsetLeft;
      const endY = event.clientY - graph.offsetTop;
      
      edge.style.left = `${startX}px`;
      edge.style.top = `${startY}px`;
      edge.style.width = `${endX - startX}px`;
      edge.style.height = `${endY - startY}px`;
      edge.style.opacity = 0.5;
    }
    
    function finishEdge(event) {
      nodes.forEach(node => {
        const rect = node.getBoundingClientRect();
        const x = event.clientX - graph.offsetLeft;
        const y = event.clientY - graph.offsetTop;
        
        if (x >= rect.left && x <= rect.right && y >= rect.top && y <= rect.bottom && node !== event.target) {
          const edge = document.createElement("div");
          edge.classList.add("edge");
          edge.style.left = `${startX}px`;
          edge.style.top = `${startY}px`;
          edge.style.width = `${node.offsetLeft - startX + node.offsetWidth / 2}px`;
          edge.style.height = `${node.offsetTop - startY + node.offsetHeight / 2}px`;
          graph.appendChild(edge);
        }
      });
      
      edge.remove();
      document.removeEventListener("mousemove", drawEdge);
      document.removeEventListener("mouseup", finishEdge);
    }
  });
});
