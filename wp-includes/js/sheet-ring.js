document.addEventListener("DOMContentLoaded", function () {
  const pills = document.querySelectorAll(
    ".scalable-systems-output-pill:not(.emphasis-pill)",
  );

  pills.forEach((pill) => {
    pill.addEventListener("click", function () {
      // 1. Remove active styling from all pills
      pills.forEach((p) => p.classList.remove("active"));

      // 2. Add active styling to the clicked pill
      this.classList.add("active");
    });
  });
});

document.addEventListener("DOMContentLoaded", function () {
  // Select all the rings on the page
  const rings = document.querySelectorAll(".sheets-ring");

  rings.forEach((ring) => {
    // Find all the ring icons within this specific ring
    const rings = ring.querySelectorAll(".ring-icon");
    const total = rings.length;

    rings.forEach((sat, index) => {
      // Calculate the angle. Subtract 90 degrees so the first item is always at the top
      const angle = index * (360 / total) - 90;

      // Pass the calculated angles directly into the CSS for this specific icon
      sat.style.setProperty("--angle", `${angle}deg`);
      sat.style.setProperty("--reverse-angle", `${-angle}deg`);
    });
  });
});
