#!/bin/bash
echo "Deploying to s3..."
aws --profile aws_gariany s3 sync --delete ../public s3://gariany.com
echo "Done!"
echo ""

echo "Invalidating Cloudfront"
aws --profile aws_gariany cloudfront create-invalidation --distribution-id "E1OEXPS7LRFGE" --paths "/*"
echo "Done!"
echo ""

echo "Completed."
echo ""
