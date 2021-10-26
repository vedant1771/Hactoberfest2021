const getWordCount = (text) => text.trim().split(/\s+/).length;

const calculateReadingTime = (text) => {
  if (!text) return 0;
  const wpm = 225;
  const words = getWordCount(text);
  const time = Math.ceil(words / wpm);
  return time;
};

calculateReadingTime('Lorem ipsum');
