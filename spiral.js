function drawSpiral(q) {
  if (q > 3) {
    var remaining = (q % 4) + 1;
    switch (remaining) {
      case 1:
        console.log('# '.repeat(q) + ' #'.repeat(q)+"\n");
        break;
      case 2:
        console.log('# '.repeat(q) + '###' + ' #'.repeat(q - 1)+"\n");
        console.log('# '.repeat(q) + ' #' + ' #'.repeat(q - 1)+"\n");
        break;
      case 3:
        console.log('# '.repeat(q) + '####' + ' #'.repeat(q - 1)+"\n");
        console.log('# '.repeat(q) + '# #' + ' #'.repeat(q - 1)+"\n");
        console.log('# '.repeat(q) + ' #' + ' #'.repeat(q - 1)+"\n");
        break;
      case 4:
        console.log('# '.repeat(q) + '#####' + ' #'.repeat(q - 1)+"\n");
        console.log('# '.repeat(q) + '# #' + ' #'.repeat(q - 1)+"\n");
        console.log('# '.repeat(q) + '### #' + ' #'.repeat(q - 1)+"\n");
        console.log('# '.repeat(q) + ' #' + ' #'.repeat(q - 1)+"\n");
        break;
    }
  }
  for (var i = q; i > 1; i--) {
    console.log('# '.repeat(i - 1) + '#'.repeat((q - i) * 4 + 4) + ' #'.repeat(i - 1)+"\n");
    console.log('# '.repeat(i - 1) + ' '.repeat((q - i) * 4 + 4) + ' #'.repeat(i - 1)+"\n");
  }
  console.log('#'.repeat(q));
}