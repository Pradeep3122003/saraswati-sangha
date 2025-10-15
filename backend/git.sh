git add .
git commit -m "$1"
if [ "$2" = "-p" ]; then
  echo "push"
  git push origin main
  sudo systemctl restart saraswati-sangha
fi
