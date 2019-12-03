#!/bin/bash
echo "================================================================================"
echo "Building..."
echo "================================================================================"
cd ../ && hugo && cd scripts

echo ""
echo ""
echo "> Done!"
echo ""

echo "================================================================================"
echo "Deploying to s3..."
echo "================================================================================"
aws --profile aws_gariany s3 sync --delete ../public s3://gariany.com
echo "================================================================================"
echo ""
echo ""
echo "> Done!"
echo ""

echo "================================================================================"
echo "Invalidating Cloudfront Distribution"
echo "================================================================================"
aws --profile aws_gariany cloudfront create-invalidation --distribution-id "E1OEXPS7LRFGE" --paths "/*"
echo ""
echo ""
echo "> Done!"
echo ""

echo "================================================================================"
echo "Completed."
echo "================================================================================"
echo ""
